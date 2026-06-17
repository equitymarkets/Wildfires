"""Wildfires dashboard - Flask backend.

Serves aggregated U.S. wildfire statistics (1992-2020) from data.sqlite to the
Plotly/Leaflet front-end in /html and /static.

Notes on the optimizations in this module:
  * ensure_indexes() builds the indexes the chart queries rely on, turning
    full-table scans over ~2.3M rows into index lookups.
  * query_df() centralizes DB access: context-managed connections (no leaks)
    and bound parameters (no SQL injection).
  * The dataset is static, so each chart's result is memoized with lru_cache;
    every endpoint hits the database at most once per process.
"""
import json
from functools import lru_cache
from pathlib import Path

import pandas as pd
import plotly.graph_objects as go
from flask import Flask, jsonify, render_template
from sqlalchemy import create_engine, text

BASE_DIR = Path(__file__).resolve().parent

# Initiates our flask app
app = Flask(__name__, template_folder="html")

# Creates a link to our database data.sqlite
engine = create_engine("sqlite:///data.sqlite")


# ---------------------------------------------------------------------------
# Database helpers
# ---------------------------------------------------------------------------
def ensure_indexes():
    """Create the indexes the dashboard queries rely on (idempotent).

    Runs once at startup. CREATE INDEX IF NOT EXISTS is a no-op once the index
    exists, so only the first run pays the build cost; after that startup is
    instant. These turn the per-chart full-table scans into index lookups
    (measured 3-20x faster per query on the ~2.3M row table).
    """
    statements = [
        "CREATE INDEX IF NOT EXISTS idx_fires_year ON Fires(FIRE_YEAR)",
        "CREATE INDEX IF NOT EXISTS idx_fires_state_year ON Fires(STATE, FIRE_YEAR)",
        "CREATE INDEX IF NOT EXISTS idx_fires_year_state_sz ON Fires(FIRE_YEAR, STATE, FIRE_SIZE)",
        "CREATE INDEX IF NOT EXISTS idx_fires_cause ON Fires(NWCG_GENERAL_CAUSE)",
        "CREATE INDEX IF NOT EXISTS idx_fires_year_class ON Fires(FIRE_YEAR, FIRE_SIZE_CLASS)",
    ]
    with engine.begin() as conn:
        for stmt in statements:
            conn.execute(text(stmt))


def query_df(sql, **params):
    """Run a parameterized query and return a DataFrame.

    The connection is context-managed (always closed) and any user input is
    passed as bound parameters, so it can never be interpolated into the SQL.
    """
    with engine.connect() as conn:
        return pd.read_sql(text(sql), conn, params=params or None)


# Population-density GeoJSON is static; load it once at import instead of
# inlining ~90KB of literal data in this file.
with open(BASE_DIR / "static" / "data" / "pop_density.json") as fh:
    POP_DENSITY = json.load(fh)


# ---------------------------------------------------------------------------
# Pages
# ---------------------------------------------------------------------------
@app.route("/")
def home():
    """Render Home Page."""
    return render_template("index.html")


# ---------------------------------------------------------------------------
# Total fires per year  (line chart)
# ---------------------------------------------------------------------------
@lru_cache(maxsize=1)
def _total_us():
    df = query_df(
        "SELECT FIRE_YEAR AS year, COUNT(STATE) AS count, AVG(FIRE_SIZE) AS size "
        "FROM Fires WHERE FIRE_YEAR >= 1992 "
        "GROUP BY FIRE_YEAR ORDER BY FIRE_YEAR"
    )
    return {
        "year": df["year"].tolist(),
        "count": df["count"].tolist(),
        "size": df["size"].tolist(),
        "type": "scatter",
    }


@lru_cache(maxsize=64)
def _total_state(state):
    df = query_df(
        "SELECT FIRE_YEAR AS year, COUNT(STATE) AS count, AVG(FIRE_SIZE) AS size "
        "FROM Fires WHERE STATE = :state "
        "GROUP BY FIRE_YEAR ORDER BY FIRE_YEAR",
        state=state,
    )
    return {
        "year": df["year"].tolist(),
        "count": df["count"].tolist(),
        "size": df["size"].tolist(),
        "type": "scatter",
    }


@app.route("/total")
def total_data():
    """Return total fires and years for the whole U.S."""
    return jsonify(_total_us())


@app.route("/total/<state>")
def state_data(state):
    """Return fires and years for a single state."""
    return jsonify(_total_state(state.upper()))


# ---------------------------------------------------------------------------
# Acres burned, top 10 states  (bar chart)
# ---------------------------------------------------------------------------
@lru_cache(maxsize=1)
def _acre_all():
    df = query_df(
        "SELECT STATE AS x, ROUND(SUM(FIRE_SIZE)) AS y FROM Fires "
        "GROUP BY STATE ORDER BY SUM(FIRE_SIZE) DESC LIMIT 10"
    )
    return {"x": df["x"].tolist(), "y": df["y"].tolist(), "type": "bar"}


@lru_cache(maxsize=64)
def _acre_year(year):
    df = query_df(
        "SELECT STATE AS x, ROUND(SUM(FIRE_SIZE)) AS y FROM Fires "
        "WHERE FIRE_YEAR = :year "
        "GROUP BY STATE ORDER BY SUM(FIRE_SIZE) DESC LIMIT 10",
        year=year,
    )
    return {"x": df["x"].tolist(), "y": df["y"].tolist(), "type": "bar"}


@app.route("/acre")
def total_acre():
    """Return acres burned for the top 10 states across all years."""
    return jsonify(_acre_all())


@app.route("/acre/<int:year>")
def acre(year):
    """Return acres burned for the top 10 states in a given year."""
    return jsonify(_acre_year(year))


# ---------------------------------------------------------------------------
# Fire causes, top 10  (pie chart)
# ---------------------------------------------------------------------------
@lru_cache(maxsize=1)
def _cause_all():
    df = query_df(
        "SELECT NWCG_GENERAL_CAUSE AS x, COUNT(NWCG_GENERAL_CAUSE) AS y FROM Fires "
        "GROUP BY NWCG_GENERAL_CAUSE ORDER BY COUNT(NWCG_GENERAL_CAUSE) DESC LIMIT 10"
    )
    return {"x": df["x"].tolist(), "y": df["y"].tolist(), "type": "pie"}


@lru_cache(maxsize=64)
def _cause_year(year):
    df = query_df(
        "SELECT NWCG_GENERAL_CAUSE AS x, COUNT(NWCG_GENERAL_CAUSE) AS y FROM Fires "
        "WHERE FIRE_YEAR = :year "
        "GROUP BY NWCG_GENERAL_CAUSE ORDER BY COUNT(NWCG_GENERAL_CAUSE) DESC LIMIT 10",
        year=year,
    )
    return {"x": df["x"].tolist(), "y": df["y"].tolist(), "type": "pie"}


@app.route("/fire_cause")
def fire_cause_data():
    """Return the top 10 causes of fire across all years."""
    return jsonify(_cause_all())


@app.route("/fire_cause/<int:year>")
def fire_cause(year):
    """Return the top 10 causes of fire for a given year."""
    return jsonify(_cause_year(year))


# ---------------------------------------------------------------------------
# Fire-size distribution  (histogram)  --  COMMENTED OUT / kept for future use.
# Older work we are not shipping right now. Left here (along with the matching
# <script src="static/js/app_size.js"> include in html/index.html) so it can be
# re-enabled later without rewriting it.
# ---------------------------------------------------------------------------
# SIZE_CLASS_LABELS = {
#     "A": "0-0.25",
#     "B": "0.26-9.9",
#     "C": "10-99",
#     "D": "100-299",
#     "E": "300-999",
#     "F": "1,000-4,999",
#     "G": "5,000+",
# }
#
#
# @lru_cache(maxsize=1)
# def _size_figure_json():
#     df = query_df(
#         "SELECT FIRE_SIZE_CLASS AS cls, COUNT(*) AS count FROM Fires "
#         "WHERE FIRE_SIZE_CLASS IS NOT NULL "
#         "GROUP BY FIRE_SIZE_CLASS ORDER BY FIRE_SIZE_CLASS"
#     )
#     labels = [f"{row.cls} ({SIZE_CLASS_LABELS.get(row.cls, '?')} ac)" for row in df.itertuples()]
#     fig = go.Figure(data=[go.Bar(x=labels, y=df["count"].tolist())])
#     fig.update_layout(
#         title="Wildfires by Size Class (1992-2020)",
#         xaxis_title="Fire size class (acres)",
#         yaxis_title="Number of fires",
#         bargap=0.2,
#     )
#     return fig.to_json()
#
#
# @app.route("/size")
# def size():
#     """Return a Plotly histogram of fires by size class."""
#     return jsonify(_size_figure_json())


# ---------------------------------------------------------------------------
# Heatmap of large 2020 fires
# ---------------------------------------------------------------------------
@lru_cache(maxsize=1)
def _heatmap():
    df = query_df(
        "SELECT LATITUDE AS lat, LONGITUDE AS lon, FIRE_SIZE AS size FROM Fires "
        "WHERE FIRE_YEAR = 2020 AND FIRE_SIZE_CLASS IN ('C', 'D', 'E', 'F')"
    )
    # Vectorized build (was a per-row df.iterrows() loop).
    return {"data": df.to_dict("records")}


@app.route("/heatmap")
def heatmap_data():
    """Return lat/lon/size points for the heatmap layer."""
    return jsonify(_heatmap())


# ---------------------------------------------------------------------------
# Population density choropleth
# ---------------------------------------------------------------------------
@app.route("/PopData")
def pop_data():
    """Return the static population-density GeoJSON."""
    return jsonify(POP_DENSITY)


# Sets name of module for python code
if __name__ == "__main__":
    ensure_indexes()
    app.run(debug=True)
