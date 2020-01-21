# boston_group

## 1. Abstract of Project
(EV)olve Boston provides data and analysis for policymakers and citizens to understand the EV transition in Boston. We examine the environmental benefits of electric vehicle expansion, the obstacles standing in the way, and the implications of that expansion on the municipal budget.

## 2. Members
Adam Staveski, Christine Peterson, Koshi Murakoshi, and Rees Sweeney-Taylor completed original research and compiled the website.

## 3. How to Run on Local Computer
* git clone git@github.com:cpeterson1105/boston_group.git
* cd to do cloned directory
* Use command "python3 -m http.server"

## 4. Data and Back End Information

### Home Page
+ 2019 Boston Climate Action Plan link: https://www.boston.gov/sites/default/files/embed/file/2019-10/city_of_boston_2019_climate_action_plan_update_4.pdf
+ Bubble chart source code available at: https://observablehq.com/@d3/bubble-chart
+ Data for bubble chart drawn from this white paper: https://theicct.org/sites/default/files/publications/US_charging_Gap_20190124.pdf

### Environmental Benefits Page
[CO2 Emissions work]  
+ All calculations are shown here: https://docs.google.com/spreadsheets/d/1qUnEusdss9Gdjh6vu9j8jQ-2b3CUyGeW6LfqbmbJmcI/edit?userstoinvite=murakoshi.koshi@gmail.com&ts=5e1cf01e#gid=0
+ CO2 to deforestation equivalency numbers are found here: https://www.sfmcanada.org/images/Publications/EN/C02_Sink_EN.pdf
+ CO2 emissions in terms of miles per gallon are found here: https://www.epa.gov/greenvehicles/greenhouse-gas-emissions-typical-passenger-vehicle
+ Deforestation assumption was based on the assumption of 150 trees per acre--an average of the 100-200 trees per acre indicated here: http://www.sbcounty.gov/calmast/sbc/html/healthy_forest.asp

[Projection of EVs in Boston]
+ All calculations are shown in /data/ev_num_bar_input_transition.xlsx
+ According to the Go Boston 2030 report (page 75), there were 351 EVs in Boston in 2015.   (https://www.boston.gov/sites/default/files/file/document_files/2019/06/go_boston_2030_-_full_report.pdf)
+ We used Figure 1.1 in the International Energy Agency's Global EV Outlook 2019 (https://www.iea.org/reports/global-ev-outlook-2019) to find the global growth of electric vehicles between 2013-2018. We used figure 2 of this same report to find the global growth prediction between 2018-2030. We applied the global growth rate to Boston's stock of EVs in 2015 to estimate future growth of EVs in the Boston market.
+ The data from the International Energy Agency's Global EV Outlook 2019 can be downloaded here:
https://iea.blob.core.windows.net/assets/8f860fa0-5f15-4d0a-8b46-8270b22984c3/GEVO-2019-Figures.zip
+ We converted the IEA data into a CSV file using Microsoft Excel. We then visualized the data using a D3 bar chart based on the following template: https://bl.ocks.org/d3noob/bdf28027e0ce70bd132edc64f1dd7ea4

[CO2 emission projection in Boston]
+ All calculations are shown in data/ev_co2_bar_input_transition.xlsx
+ The Metropolitan Area Planning Council's Massachusetts Vehicle Census estimates the number of households in Boston in 2013 at 25,926 (see hh_est in https://www.mapc.org/learn/data/). 
+ The Massachusetts Vehicle Census also estimates the average emissions per household per day as 0.098 metric tons (see co2eqv_hh_CO2 in https://www.mapc.org/learn/data/).
+ By multiplying (number of households)x(average emissions per day)x(365 days) we estimate total CO2 emissions in the city of Boston in 2014 as 927,359 metric tons. 
+ The data for the above calculation can be downloaded from: https://mapc-org.sharefile.com/d-s32d7ffdf5514fca9
+ According to Figure 5 in the International Energy Agency's Global EV Outlook 2019, we can find the global projection of CO2 emissions. We estimate the reduction ratio from the use of EVs as: Reduction ratio = Avoided GHG emissions / (‘GHG emissions from whole transport sector’ + ‘Avoided GHG emissions’). 
+ We assumed emissions in 2014 were the same as emissions in 2018 (927,359 MtCO2-eq) and applied the global EV transition ratio and global reduction ratio to estiamte CO2 emission reduction in Boston. 
+ We made a CSV dataset using Microsoft Excel and then used Datawrapper (https://www.datawrapper.de/) to visualize. 

### Obstacles Page
[Obstacles to Electric Vehicle Ownership]
+ The Ratio of Electric Vehicles to Electric Vehicle Chargers
* We downloaded all state data from this website: https://evadoption.com/ev-charging-stations-statistics/charging-stations-by-state/
* We computed data for Boston by using our projection of EVs in Boston in 2019 and manually counting the total number of charging stations in Boston based on data from Plugshare (https://www.plugshare.com/). We applied the formula: (Our projection of EVs in 2019) / (hand-counted EV charging ports from Plugshare)
* We cited a survey from the Recharge Boston website (https://www.boston.gov/departments/transportation/recharge-boston-electric-vehicle-resources).

[Current Electric Vehicle Charging Stations]
+ We got the budgetary information from the Boston's Capital Budget FY 2020-2024 (https://data.boston.gov/organization/office-of-budget-management)

[Planned Expansion of Electric Vehicle Charging Stations]
+ We pulled this image from the Recharge Boston website (https://www.boston.gov/departments/transportation/recharge-boston-electric-vehicle-resources).

[Future Opportunities For Electric Vehicle Charging Stations]
+ We used ARCGIS to add blue marks where the city plans to expand its publicly availble charging stations. We searched the address and used the ‘Add to Map Notes’ function (http://arcg.is/0mevm4). 
+ We then visually inspected the map and used Microsoft PowerPoint to add red circles to areas without charging stations. 

### Budgetary Consequences Page
[The City's Budget Does Not Prioritize Electric Vehicles]
+ We downloaded budgetary information from the Boston's Capital Budget FY 2020-2024 (https://data.boston.gov/organization/office-of-budget-management).
+ Using Excel, we deleted every column except 'Department', 'Project Name', and 'Total Project Budget'. 
+ Using an Excel formula ... =IF(A2=A1,"",SUMIF(A:A,A2,C:C)) ... we compiled the total sum of each agency's capital investments. We used an Excel sort function to sort the agencies in order of most planned capital investment to least planned capital investment.
+ We scanned all projects to find those which related to electric vehicles. Only one such project existed--the Transportation Department's "Electric Charging Stations" project which had $300,000 of planned investment.
+ We spoke on the phone with employees from the city of Boston who told us that the project was expected to produce 18 new electric charging stations and 36 new electric charging ports.

[The Transportation Department Does Not Prioritize Electric Vehicles]
+ We downloaded budgetary information from the Boston's Capital Budget FY 2020-2024 (https://data.boston.gov/organization/office-of-budget-management).
+ Using the same method as above, we summed all planned investments allocated to the Transportation Department--this number amounted to $123 million. 
+ The share of all projects that are car-centric was obtained by visually scanning and doing some minor research into each of the Transportation Department's 30 planned investments. We found that $97.1 million was devoted to car-centric projects, $19.5 million was devoted to walking/biking-centric projects, and $6.7 million was devoted to other miscellaneous projects.

[The City Must Invest More In Electric Vehicles]
+ In order to maintain the same ratio of EVs to EV charging stations that currently exists requires the City of Boston to build 1,800 additional charging stations by 2030. This is based on the current ratio of EVs to EV charging stations constructed above and the projected growth in EVs in Boston, which is also constructed above.
+ We spoke on the phone with employees from the City of Boston who told us that EV site installation can cost between $80,000 and $100,000 per site and that each individual charging station costs roughly $6,000.
+ We then computed the estimated necessary investment by multiplying (1,800 necessary charging stations)x($6,000 per station)x(120 estimated new site installations) = $21.6 million.
+ Using a naive extrapolation of the city's budget based on data found on the city's website (https://data.boston.gov/dataset/adopted-operating-budget), I estimated that the City of Boston's 10-year budget is $3.5 billion. Assuming a necessary $21.6 million investment, this amounts to less than 0.01% of the overall 10-year budget.
