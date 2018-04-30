# Cost of Living in the US
## Michelle Deng, Yulin Liu, Elizabeth Onstwedder

https://elizabeth247.github.io/

TODO: Screencast video is here.

Cost of living is often used to compare how expensive it is to live in one city versus another locale (Investopedia). 
With us graduating and moving to different cities in the country, we hope to develop a tool that helps budget planning by presenting how expenses differ across cities. 

Our visualization is a simple one-page visualization coded primarily with D3 and a tiny bit of JQuery. It contains a map with the positions of 26 cities highlighted with red dots. Hovering over a dot shows a tooltip with the city, state, and that city's corresponding cost of living index and its cost of living index including rent. We used Numbeo's API for this data, so the cost of living indices are calculated in comparison to New York, New York. Thus, New York's cost of living indices are 100, and all other cities' cost of living indices are calculated relative to 100. 

Clicking on any of the red dots will render a pie chart to the right of the map, breaking down proportions for transportation, food and entertainment, and rent for the city that was clicked. 

Below the map, users can directly compare the average costs of food and entertainment, transport, and rent prices between two cities. 

All of our code can be found in `index.html`, the data files we used for this visualization are: `26citiesWithLatitudeLongitude.csv`, `cityCostOfLiving.csv`, and `us-states.json`, we cleaned and organized some of our data with a Python script called `dataprocessing.py`, and our initial data scraping scripts and data files can be found [here]("https://github.com/mddengo/data-viz-final"): https://goo.gl/HzVBMr.
