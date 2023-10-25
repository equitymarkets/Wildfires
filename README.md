# Wildfires

<img width="100%" alt="Wildfires!" src="https://user-images.githubusercontent.com/119274891/231022049-302a84df-2d5d-4e94-840b-5a9cc1c25437.png">

<img width="100%" alt="Wildfires in the US header" src="https://user-images.githubusercontent.com/119986667/234643307-ed473ea7-cbdf-41a2-8ae0-e06bc5f1729d.png">

## Welcome! We've gathered data from Kaggle that includes 2.3 million fires in the country from 1992 to 2020. Continue scrolling for an in-depth study of whether or not fires have become larger or more widespread in the last 30 years.

## Want to run our app for yourself? Just clone the project and run app.py from the local directory. You will also need to paste the data.sqlite file available from the Kaggle wildfire dataset [here](https://www.kaggle.com/datasets/behroozsohrabi/us-wildfire-records-6th-edition).

# As areas have increased in population, do we see a proportional increase in fires? 

### We chose to tackle this question because we are aware of the disastrous effects of wildfires across the United States; particularly in the West. Our dataset hinges on geographical locations, and we had hypothesized that less populated areas would have larger fires. With less people in these areas, there would be a smaller amount of people in immediate danger, so to save human lives and resources, we theorized that they would let the fires burn, and thus the fires would spread over more acres. See below where we share our findings!

### Acres Burned (Top 10 States)

 <img width="100%" alt="Wildfires by State" src="https://user-images.githubusercontent.com/119986667/234644208-b5c33c13-900e-4c46-b5af-35ab655dcce8.png">

  * To begin, our first image shows total acreage burned across the top 10 states, across all years. Evidently, Alaska has had the most acres burned as a result of wildfires. This devastating range of fire damage only increased our curiosity of just how much worse fires are getting each year.

### Number of Fires (Average vs. Total)

 <img width="100%" alt="Average Fire Size vs. Total" src="https://user-images.githubusercontent.com/119986667/234644471-966d9b94-118f-4da8-ad26-69c5fbcae8ac.png">

  * This graph shows the total number of wildfires and average fire size for each year, from 1992 to 2020. When we say average fire size, we mean the average acreage a wildfire burns. The purpose of this graph is to get a sense of whether wildfires are increasing each year, as well as to uncover if the wildfires are getting worse or burning more area than before.

  * To analyze this, we used the Pearson Correlation Test to see if there is a relationship between time and number of fires/ average fire size. When we ran the test, we found there was no statistically significant correlation between years and number of fires. However, when we ran the test with years and average fire size, we found a positive correlation between the two. Thus, we can conclude that as we’ve moved forward from 1992, there was no significant change in the total number of fires, but the average fire size has increased; which means the fires are burning across more acres.

  * All things considered, this does not explain why the average fire has gotten worse from 1992. Continue scrolling to explore more possible causes of this trend!

### Top 10 Causes of Wildfires

<img width="100%" alt="Causes of Wildfires" src="https://user-images.githubusercontent.com/119986667/234644692-70a20c05-d806-480f-96a6-7f02eabb3f59.png">

  * Here we have a chart representing the Top 10 causes of wildfires in the United States. We can see here that debris and open burning make up about a quarter of wildfires in the United States. Two other leading causes are natural and arson--both at around 14%--which represent the two extremes of acceptability within the range of data. 

  * Other small causes include equipment and vehicle use, recreation or ceremony, misuse of fire by minors, smoking, railroad use, and power generation.

  * Many fires inevitably occur in areas of little or no population, as we will see in the heat map below. There are many reasons why local fire departments may hesitate to or be unable to extinguish these usually large fires that are away from settled or agricultural areas. Just a few include: 

    * The risk of life-threatening injuries to firefighters during the fire control process may be high. 

    * The infrastructure in local and regional fire departments might not support extinguishing large fires. 

    * The use of them might leave other populated areas vulnerable to emergencies. 

  * Wilderness wildfires in some instances are considered a part of the natural environmental process, necessary to the growth of native species, such as is the case with the longleaf pine of the coastal Southeast US. In all the above cases, we can see why the priority of fire departments might be to simply monitor, or at most control, large fires away from populated areas.
  
  * We also see here the number of data points for unknown causes, and indeed recently we can see that this number is higher even than the historical average. Although it was not the primary focus of our study, we note that we did discuss this limitation in the data.

  * The preceding in mind, the point of the study was not to assume that every fire is “bad”, question why some large fires are left to burn, nor speculate on the motive of each fire department across 30+ years of data. We want the data to speak for itself.

  * The data below will further explore our assumptions that small fires often occur near human settlements, are often caused by humans, and are extinguished fairly quickly, while larger fires, which occur much less in frequency, often occur farther from human settlement, have both human and natural causes (mostly natural), and grow much larger in size due to their distance from populated centers.

### Summary Statistics

<img width="100%" alt="Human vs. Natural Size and Cause" src="https://user-images.githubusercontent.com/119986667/234645071-745660cc-8897-474b-ac53-d41b59f67d06.png">

<img width="100%" alt="Counts Over Time and by State" src="https://user-images.githubusercontent.com/119986667/234645250-95aed9dd-0073-4994-86b0-c166f153d030.png">

  * The count of fire is the same over the years.

  * The average size in fire increased over the years. 

  * The biggest "Cause" category in fire size is naturally caused fires

  * The largest fire size state in the top ten states, by land area.

  * The count of fires is highest in the human category, which might be driven by population. 

### Population Map

<img width="100%" alt="Population Map" src="https://user-images.githubusercontent.com/119986667/234646229-beda4022-b378-44dd-a8fb-3a4c32348be4.png">

  * To test our hypothesis we also wanted to look at trends with fires and population to see if perhaps people are getting closer to or moving away from areas prone to large fires. 
  
  * When looking at the heat map, we notice that other than Alaska it is evident that fire growth is most intense in the western United States. As the size of fires increases out west, our curiosity was with population movements in those areas; and there are some alarming tends. We looked at population density growth across the US from 1990 to 2020 to get a sense of where people are moving. Then we looked at those states with high rates of growth to see where they currently stand with population density in relation to the rest of the country. Three states stand out from this perspective: California, Texas, and Arizona.

  * California has been a relatively dense state for some time, and fires have historically been an issue there. What is interesting to note is it continues to grow at a moderate pace of 33%.

  * That said, it is Texas and Arizona where the alarm bells ring loudest. There is a lot of red over these states on the heat map (noting some of the largest fires) and both currently are relatively dense states at 112 and 63 people per square mile, respectively. Most notably though, both states have seen substantial growth in 30 years, with Texas growing at a 72% clip and Arizona almost doubling over that period. If these trends continue, it’s safe to expect suburban and rural sprawl to bring people closer to the largest fires.

  * What makes these numbers even more concerning is a link scientists in the Pacific Northwest are finding between Arctic ice melt and wildfires. In a nutshell: Ice melting in the Arctic is causing a change in the jet stream that pushes really hot dry air across the western United States, mostly in the fall—which presents a high risk of fires during the prime wildfire season. For more on this, visit the links from NPR on our website below. 

### Heat Map & Summary

<img width="100%" alt="Heat Map" src="https://user-images.githubusercontent.com/119986667/234646414-c06b602c-709d-4cab-9069-deaefda3c802.png">

  * Here we have our heat map which shows all fires larger than 10 acres that occurred in 2020. We chose this limit because it reduces the number of fires on the display down from roughly 73,000 to around 8,000 in 2020 alone. Mapping all 73k makes it difficult to decern any pattern to the fires because of the large number of small fires that washes the heat map out. Looking at only fires that burn more than 10 acres we can more clearly see the areas impacted by these large fires.
  
  * We started this analysis wanting to investigate what seems to be a pattern of worsening wildfires in the US. We thought this might be due to large fires in rural areas with low population, increasing numbers of fires, and larger fires overall.

  * As the data and analysis shows, we are not seeing more fires, but we are seeing larger average fires each year. All types of fires have gotten larger over time, but the increase is being driven primarily by natural causes, which is lightning in the US. Lightning accounts for only 10-15% of the total number of fires we have but is responsible for roughly 60% of the acreage burned over the last 28 years. The size of natural fires has increased almost 740% while the size of human caused fires has only gone up 160%. 

  * We also see a connection between rural land areas and large natural fires, but the population is growing in these areas, which is leading to increased devastation and human costs. So while humans are not starting these huge devastating fires, they are suffering from them. 

  * It would be interesting to follow this data over the next several years to see how continued population increases in previously rural areas, changes in climate, and evolving fire management strategies will impact the size and number of fires we see as well as the toll they take on people.

#### Resources

<img width="100%" alt="Resources" src="https://user-images.githubusercontent.com/119986667/234646664-0f5c6e04-e334-4ce9-8001-0956e51cc235.png">

  * [Historical Population Density Data (1910-2020)](https://www.census.gov/data/tables/time-series/dec/density-data-text.html)

  * [Project Dataset - 2.3 Million US Wildfires((1992-2020))](https://www.kaggle.com/datasets/behroozsohrabi/us-wildfire-records-6th-edition)

  * [NPR - Wildfires are bigger. Arctic ice is melting. Now, scientists say they're linked : Short Wave](https://www.npr.org/2023/04/12/1169471568/wildfires-are-bigger-arctic-ice-is-melting-now-scientists-say-theyre-linked)
  
  * [The surprising connection between Arctic ice and Western wildfires](https://apps.npr.org/arctic-ice-melting-climate-change/western-us-wildfires.html)
  
  * [The Longleaf Pine](https://www.nature.org/en-us/what-we-do/our-priorities/protect-water-and-land/land-and-water-stories/longleaf-pine-restoration/)

  * [What Causes Wildfires?](https://wfca.com/articles/what-causes-wildfires/?gclid=CjwKCAjw0ZiiBhBKEiwA4PT9z8dFK3tNWDmkAs6JNVatK31HVNVUnE0RhSPb1d-GXy4Uw0Db4Q_O7xoCN0UQAvD_BwE) 

## THANK YOU FOR VISITING OUR SITE, COME BACK SOON!🔥
