# boston_group

1. Abstract of project: 
This website (EVolve Boston) provides data and analysis for policymakers and citizens to understand the EV transition in Boston. Forcusing on the user story of "employee of Recharge Boston", this website shows a environmental benefis of EVs, obstacles to promote Evs, budgetary considerations.  

2. Members: 
Adam Staveski
Christine Peterson
Koshi Murakoshi
Rees Sweeney-Taylor

3. How to run in local computer: 
-git clone git@github.com:cpeterson1105/boston_group.git
-cd to do cloned dictionary
-Use command "python3 -m http.server"

4. Data and Back end information
=Home=
2019 Boston Climate Action Plan Link: https://www.boston.gov/sites/default/files/embed/file/2019-10/city_of_boston_2019_climate_action_plan_update_4.pdf
Bubble chart source code available at:
https://observablehq.com/@d3/bubble-chart
Data for bubble chart drawn from this white paper:
https://theicct.org/sites/default/files/publications/US_charging_Gap_20190124.pdf


=Environmental Benefits=
[CO2 Emissions work]
All calculations are shown here: https://docs.google.com/spreadsheets/d/1qUnEusdss9Gdjh6vu9j8jQ-2b3CUyGeW6LfqbmbJmcI/edit?userstoinvite=murakoshi.koshi@gmail.com&ts=5e1cf01e#gid=0
CO2 to deforestation equivalency numbers are found here: https://www.sfmcanada.org/images/Publications/EN/C02_Sink_EN.pdf
CO2 Emissions by mile/gallon are found here: https://www.epa.gov/greenvehicles/greenhouse-gas-emissions-typical-passenger-vehicle
General conversions were googled (hectare to acre for example)
Using the assumption of 150 trees per acre based on the average being 100-200 indicated below (before thinning occurs)
“The problem fire protection officials face is that not only does green vegetation burn, the forest is overstocked — 100 to 200 trees per acre, where a healthy forest has 40 to 60 trees per acre.” http://www.sbcounty.gov/calmast/sbc/html/healthy_forest.asp
Boston compared to U.S. Cities work
https://theicct.org/publications/charging-gap-US
Appendix at the bottom has values used for EV numbers
Population of U.S. metropolitan areas information found here: https://www.statista.com/statistics/183600/population-of-metropolitan-areas-in-the-us/
All compiled here: https://docs.google.com/spreadsheets/d/1qUnEusdss9Gdjh6vu9j8jQ-2b3CUyGeW6LfqbmbJmcI/edit?userstoinvite=murakoshi.koshi@gmail.com&ts=5e1cf01e#gid=232761710

[Projection of EVs in Boston]
All calculations are shown here (Sheet, EVs_Boston_Projection).  https://drive.google.com/open?id=1v4dYkn06bRgfEojvpzGuHX2GFPPWZzcq
According to the Go Boston 2030 report pp.75, the number of EVs in Boston, 2015, is 351.   (https://www.boston.gov/sites/default/files/file/document_files/2019/06/go_boston_2030_-_full_report.pdf)
According to Global EV Outlook 2019, Figure 1.1 , we can find the global growth of electric vehicles stock between 2013-2018. Also, Figure 2 shows the global growth prediction between 2018-2030. We applied the global growth ratio to the number of EVs in boston, 2015 to estimate the future projection. https://www.iea.org/reports/global-ev-outlook-2019
We can download excel data of all figures from here. 
https://iea.blob.core.windows.net/assets/8f860fa0-5f15-4d0a-8b46-8270b22984c3/GEVO-2019-Figures.zip
We converted this data into csv file by excel. Then, visualized in bar chart by D3 template(https://bl.ocks.org/d3noob/bdf28027e0ce70bd132edc64f1dd7ea4). 

[Projection of CO2 emission in Boston]
All calculations are shown here (Sheet, CO2_Boston_Projection).  https://drive.google.com/open?id=1v4dYkn06bRgfEojvpzGuHX2GFPPWZzcq
According to the Metropolitan Area Planning Council’s Massachusetts Vehicle Census, we can find 1) the estimated number of house hold in Boston, 2013 as 25, 926 in the column ‘hh_est’ and 2) per Day per Household(metric tonnes of CO2 equivalent) as 0.098 in the column ‘co2eqv_hh_CO2’. By multiplying these numbers and 365, we estimate CO2 emissions in Boston, 2014 as 927,359 MtCO2-eq. 
Source　https://www.mapc.org/learn/data/
We can download metadata and zipdata fro here. 
https://mapc-org.sharefile.com/d-s32d7ffdf5514fca9
According to the Global EV Outlook 2019, Figure 5, we can find the global projection of CO2 emission. By using the ‘GHG emissions from whole transport sector’ and ‘Avoided GHG emissions’, we estimated the ratio of avoided emissions between 2018-2030 as below. 
Reduction ratio = Avoided GHG emissions / (‘GHG emissions from whole transport sector’ + ‘Avoided GHG emissions’). 
By assuming 2014 emission amount in Boston as 2018 emission amount (927,359 MtCO2-eq), we applied the global transition ratio of total CO2 emission and reduction ratio to 927,359 MtCO2-eq. 
We made csv dataset by excel and used the datawrapper(https://www.datawrapper.de/) to visualize. 

=Obstacles Page=
In Boston, there are approximately eight electric vehicle charging stations for every electric vehicle. This compares favorably to the national statewide median of 11 electric vehicles per charging station. But while Boston's vehicle-to-charger ratio is currently above average, it needs to continue to invest in charging stations if it hopes to keep up with strong projected growth of consumer demand.
I got all the state data from this website(https://evadoption.com/ev-charging-stations-statistics/charging-stations-by-state/)
I computed the Boston data as: (Our projection of EVs in 2019) / (hand-counted EV charging ports from Plugshare)

There are an estimated 3,055 electric vehicles in Boston, compared with an estimated 380 publicly available charging stations. This presents a challenge for current and potential electric vehicle owners. Although this compares favorably with the national average, it is important to maintain a similar ratio of vehicles to charging station going forward. This will require considerably more investment than is currently being devoted in the city of Boston's Capital Plan.
I got all the state data from this website(https://evadoption.com/ev-charging-stations-statistics/charging-stations-by-state/)
I computed the Boston data as: (Our projection of EVs in 2019) / (hand-counted EV charging ports from Plugshare)

Maintaining a low ratio of electric vehicles to electric vehicle charging stations is essential to ensuring that electric vehicles are a viable method of transportation. A lack of publicly accessible charging stations increases the likelihood that a driver running low on charge will become stranded away from their home. It also increases the inconvenience of owning an electric vehicle. In fact, a survey conducted as part of the city of Boston's 2019 Climate Action Plan found that 45 percent of Boston residents would purchase an electric vehicle if they knew they had access to a charging port.
I got this information from the Recharge Boston website(https://www.boston.gov/departments/transportation/recharge-boston-electric-vehicle-resources)

“Over the next five years, the city of Boston plans to spend $300,000 to expand the number of electric vehicle charging stations in municipal lots. Each of the six lots pictured below is slated to receive between four and six additional charging ports by the end of FY 2024.”
I got the budgetary information from the Capital Budget(https://data.boston.gov/organization/office-of-budget-management)

[Future Opportunities For Electric Vehicle Charging Stations]
This map added the planned charging station as blue mark on Arc Gis map by searching the address and ‘Add to Map Notes’ function. ’(http://arcg.is/0mevm4). 
Copied the map with blue mark as image file. Then, add red circles on areas without charging stations by using powerpoint. 

=Budgetary Consequences Page=
As part of its Capital Budget for FY 2020-2024, the city of Boston committed $300,000 to expanding the number of electric vehicle charging stations in municipal lots. While this may sound like a lot, the proposal will create just 18 new electric vehicle charging stations (corresponding with 36 electric vehicle charging ports) over the next five years.
I got the budgetary information from the Capital Budget
I got the 18/36 numbers from the folks we spoke with on the phone


The investment in electric vehicles includes an initial $100,000 investment in FY 2020 and an additional $200,000 investment over the FY 2021-2024 period. The investment is appropriated through the city's Transportation Department, which is currently slated to receive over $123 million in capital investment over the next five years. Although that sum is sixth-most among municipal agencies, the Transportation Department receives less investment than the Department of Parks and Recreation and the Boston Public Library. The Department of Environment is receiving even less investment--just over $61 million over the next five years. Every public dollar spent is a choice and the city's current Capital Plan does not prioritize fleet electrification or other environmental goals.
I got the budgetary information from the Capital Budget


The city of Boston plans to invest $123 million in the Transportation Department over the next five years. Of that planned investment, 79 percent is car-centric. And yet, investments in electric vehicles compose just 0.2 percent of overall transportation investments over the next five years. Although many of the city's car-centric transportation investments are worthwhile measures to improve the safety of the city's roadways, there is still a striking lack of investment in electric vehicles. Of the Transportation Department's 30 capital investment projects, just one is related to electric vehicles.
I got the budgetary information from the Capital Budget
The 79 percent figure/0.2 percent figure I calculated by hand using the Capital Budget data
I counted the 30 capital investments on the spreadsheet as well

“This will cost approximately $21.6 million.”
This number is definitely the sketchiest of the bunch. I took the projected 1,800 necessary charging stations and subtracted the number of charging stations Koshi estimated existed today. I multiplied that number by 6,000. I then added on an estimate of the additional cost of site installation. I think I estimated that a new site would need to be built for every 10 ports (5 stations).
“In addition to installation costs, which can range from $80,000 to $100,000 per site, the equipment for each EV charging site can cost up to $6,000.”
This information comes from the fine folks we spoke with on the phone.
“While this might sound like a lot, it is less than 0.01% of the city's 10-year budget.”
I found information about the city’s budget here. I then took the estimated $21.6 million and divided it by the city’s $3.5 billion budget times 10 years. This is a gross underestimate of the budget, I’m sure, but I was a bit pressed for time.

