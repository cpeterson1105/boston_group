# boston_group

##1. Abstract of project
This website (EVolve Boston) provides data and analysis for policymakers and citizens to understand the EV transition in Boston. Forcusing on the user story of "employee of Recharge Boston", this website shows a environmental benefis of EVs, obstacles to promote Evs, budgetary considerations.  

##2. Members
Adam Staveski, Christine Peterson, Koshi Murakoshi, Rees Sweeney-Taylor

##3. How to run in local computer
* git clone git@github.com:cpeterson1105/boston_group.git
* cd to do cloned dictionary
* Use command "python3 -m http.server"

##4. Data and Back end information

###Home Page
2019 Boston Climate Action Plan Link: https://www.boston.gov/sites/default/files/embed/file/2019-10/city_of_boston_2019_climate_action_plan_update_4.pdf
Bubble chart source code available at:
https://observablehq.com/@d3/bubble-chart
Data for bubble chart drawn from this white paper:
https://theicct.org/sites/default/files/publications/US_charging_Gap_20190124.pdf

###Environmental Benefits Page
[CO2 Emissions work]  
+ All calculations are shown here: https://docs.google.com/spreadsheets/d/1qUnEusdss9Gdjh6vu9j8jQ-2b3CUyGeW6LfqbmbJmcI/edit?userstoinvite=murakoshi.koshi@gmail.com&ts=5e1cf01e#gid=0
+ CO2 to deforestation equivalency numbers are found here: https://www.sfmcanada.org/images/Publications/EN/C02_Sink_EN.pdf
+ CO2 Emissions by mile/gallon are found here: https://www.epa.gov/greenvehicles/greenhouse-gas-emissions-typical-passenger-vehicle
+ General conversions were googled (hectare to acre for example)
+ Using the assumption of 150 trees per acre based on the average being 100-200 indicated below (before thinning occurs)
+ “The problem fire protection officials face is that not only does green vegetation burn, the forest is overstocked — 100 to 200 trees per acre, where a healthy forest has 40 to 60 trees per acre.” http://www.sbcounty.gov/calmast/sbc/html/healthy_forest.asp

[Projection of EVs in Boston]
+ All calculations are /data/ev_num_bar_input_transition.xlsx
+ According to the Go Boston 2030 report pp.75, the number of EVs in Boston, 2015, is 351.   (https://www.boston.gov/sites/default/files/file/document_files/2019/06/go_boston_2030_-_full_report.pdf)
+ According to Global EV Outlook 2019, Figure 1.1 , we can find the global growth of electric vehicles stock between 2013-2018. Also, Figure 2 shows the global growth prediction between 2018-2030. We applied the global growth ratio to the number of EVs in boston, 2015 to estimate the future projection. https://www.iea.org/reports/global-ev-outlook-2019
+ We can download excel data of all figures from here. 
https://iea.blob.core.windows.net/assets/8f860fa0-5f15-4d0a-8b46-8270b22984c3/GEVO-2019-Figures.zip
+ We converted this data into csv file by excel. Then, visualized in bar chart by D3 template(https://bl.ocks.org/d3noob/bdf28027e0ce70bd132edc64f1dd7ea4). 

[CO2 emission projection in Boston]
+ All calculations are shown in data/ev_co2_bar_input_transition.xlsx
+ According to the Metropolitan Area Planning Council’s Massachusetts Vehicle Census, we can find 1) the estimated number of house hold in Boston, 2013 as 25, 926 in the column ‘hh_est’ and 2) per Day per Household(metric tonnes of CO2 equivalent) as 0.098 in the column ‘co2eqv_hh_CO2’. By multiplying these numbers and 365, we estimate CO2 emissions in Boston, 2014 as 927,359 MtCO2-eq. 
+ Source　https://www.mapc.org/learn/data/  
We can download metadata and zipdata fro here.  
https://mapc-org.sharefile.com/d-s32d7ffdf5514fca9
+ According to the Global EV Outlook 2019, Figure 5, we can find the global projection of CO2 emission. By using the ‘GHG emissions from whole transport sector’ and ‘Avoided GHG emissions’, we estimated the ratio of avoided emissions between 2018-2030 as below. 
* Reduction ratio = Avoided GHG emissions / (‘GHG emissions from whole transport sector’ + ‘Avoided GHG emissions’). 
+ By assuming 2014 emission amount in Boston as 2018 emission amount (927,359 MtCO2-eq), we applied the global transition ratio of total CO2 emission and reduction ratio to 927,359 MtCO2-eq. 
+ We made csv dataset by excel and used the datawrapper(https://www.datawrapper.de/) to visualize. 

###Obstacles Page
[Obstacles to Electric Vehicle Ownership]
+Paragraph 1
* We got all the state data from this website(https://evadoption.com/ev-charging-stations-statistics/charging-stations-by-state/)
* I computed the Boston data as: (Our projection of EVs in 2019) / (hand-counted EV charging ports from Plugshare)

+ Paragraph 2
* We got all the state data from this website(https://evadoption.com/ev-charging-stations-statistics/charging-stations-by-state/)
* We computed the Boston data as: (Our projection of EVs in 2019) / (hand-counted EV charging ports from Plugshare)

+ Paragraph 3
* We got this information from the Recharge Boston website(https://www.boston.gov/departments/transportation/recharge-boston-electric-vehicle-resources)

[The Ratio of Electric Vehicles to Electric Vehicle Chargers]
+ https://theicct.org/publications/charging-gap-US
+ Appendix at the bottom has values used for EV numbers
+ Population of U.S. metropolitan areas information found here: https://www.statista.com/statistics/183600/population-of-metropolitan-areas-in-the-us/
+ All compiled here: https://docs.google.com/spreadsheets/d/1qUnEusdss9Gdjh6vu9j8jQ-2b3CUyGeW6LfqbmbJmcI/edit?userstoinvite=murakoshi.koshi@gmail.com&ts=5e1cf01e#gid=232761710

[Current Electric Vehicle Charging Stations]
+ We got the budgetary information from the Capital Budget(https://data.boston.gov/organization/office-of-budget-management)

[Future Opportunities For Electric Vehicle Charging Stations]
+ This map added the planned charging station as blue mark on Arc Gis map by searching the address and ‘Add to Map Notes’ function. ’(http://arcg.is/0mevm4). 
+ Copied the map with blue mark as image file. Then, add red circles on areas without charging stations by using powerpoint. 

###Budgetary Consequences Page
[The City's Budget Does Not Prioritize Electric Vehicles]
+ Paragraph 1
* We got the budgetary information from the Capital Budget
* We got the 18/36 numbers from the folks we spoke with on the phone

+ Paragraph 2
* We got the budgetary information from the Capital Budget(https://data.boston.gov/organization/office-of-budget-management

[The Transportation Department Does Not Prioritize Electric Vehicles]
+ Paragraph 1
* We got the budgetary information from the Capital Budget(https://data.boston.gov/organization/office-of-budget-management)
* The 79 percent figure/0.2 percent figure I calculated by hand using the Capital Budget data
* We counted the 30 capital investments on the spreadsheet as well

[The City Must Invest More In Electric Vehicles]
+ Paragraph 2 “This will cost approximately $21.6 million.”
* This number is definitely the sketchiest of the bunch. I took the projected 1,800 necessary charging stations and subtracted the number of charging stations Koshi estimated existed today. I multiplied that number by 6,000. I then added on an estimate of the additional cost of site installation. I think I estimated that a new site would need to be built for every 10 ports (5 stations).
+ “In addition to installation costs, which can range from $80,000 to $100,000 per site, the equipment for each EV charging site can cost up to $6,000.”
* This information comes from the fine folks we spoke with on the phone.
+ “While this might sound like a lot, it is less than 0.01% of the city's 10-year budget.”
* I found information about the city’s budget here(https://data.boston.gov/dataset/adopted-operating-budget). I then took the estimated $21.6 million and divided it by the city’s $3.5 billion budget times 10 years. This is a gross underestimate of the budget, I’m sure, but I was a bit pressed for time.
