## Python Rutgers Bootcamp Challenge "Project Three"  - Electric Vehicles In State of Washington

This activity is broken down into multiple deliverables to makes progress towards developing a full-stack data visualization web application that allows users to interactively explore a dataset.

## Description

In this assignment, we will need to complete the following objectives: 

Data and Delivery 

* Data components used in the project are clearly documented. 
* The dataset contains at least 100 unique records. 
* A database is used to house the data (SQL, MongoDB, SQLite, etc.). 
* The project is powered by a Python Flask API and includes HTML/CSS, JavaScript, and the chosen database
  
Back End 

* The page created to showcase data visualizations runs without error. (7.5 points)
* A JavaScript library not shown in class is used in the project. (7.5 points)

The project conforms to one of the following designs

* A Leaflet or Plotly chart built from data gathered through web scraping.
* A dashboard page with multiple charts that all reference the same data.
  
Visualizations 

* A minimum of three unique views present the data. 
* Multiple user-driven interactions (such as dropdowns, filters, or a zoom feature) are included on the final page. 
* The final page displays visualizations in a clear, digestable manner. 
* The data story is easy to interpret for users of all levels.
  
## Instructions

1. Identifying Data For Analysis

* Our group chose to select and analyze data based on  [Electric Vehicle Population Data](https://data.wa.gov/Transportation/Electric-Vehicle-Population-Data/f6w7-q2d2).

![Screenshot 2023-10-19 123414](https://github.com/Connextstrategy/Electric-Vehicles-In-Washington-State/assets/18508699/85ac7034-ca05-4c0e-b3b7-2077f3790f5a)

* This data was important as it included numerous data types to be used for visualizations in the project to include Make, Model, County, City, State, Postal Code, Electric Vehicle and EV Type

![Screenshot 2023-10-19 123431](https://github.com/Connextstrategy/Electric-Vehicles-In-Washington-State/assets/18508699/065bfd2e-dbe4-4ede-9714-98fa7e8ebbd5)

* We wanted to include data which included data on prices, range of vehicles and charge rates, so we identified [this website](https://ev-database.org)

* This enabled us to pull important data (MSRP, RapidCharge, Range, etc.) based on the previous State of Washington electric vehicles model names

![Screenshot 2023-10-19 131057](https://github.com/Connextstrategy/Electric-Vehicles-In-Washington-State/assets/18508699/6b216ab6-7fb5-427f-a708-a64aff0ad184)

2. Webscraping EV database and exporting CSV file for integrated database creation

* In order to get the data from the EV database website, we we forced to scrap the data from it via Beautiful Soup in Python and then create a dataframe off the data pulled to include the data we required for our visualizations

![Screenshot 2023-10-19 131311](https://github.com/Connextstrategy/Electric-Vehicles-In-Washington-State/assets/18508699/5fb9a08c-af9e-4228-9beb-a6b92c03e307)

![Screenshot 2023-10-19 131335](https://github.com/Connextstrategy/Electric-Vehicles-In-Washington-State/assets/18508699/052b1b48-3723-4f9b-9fb8-6b6e37d1c597)

* Following the dataframe creation we exported a clean CSV file named EV_Analysis_Database. 
  
3. Cleaning up Electric Vehicle Population Data for exporting CSV file for integrated database creation

* We need to clean up the data for the Electric Vehicle Population data from State of Washington so we did the following:
  - Dropped NAs
  - Removed years older than 2022
  - Extracted longitude and latitude data from Vehicle Location variable
  - Dropped columns not neccesary from analysis
  - Removed or extracted only models we deemed necessary for analysis
  - Matched correct Model Names with the same exact syntax from the EV_Analysis_Database
 
  ![Screenshot 2023-10-19 133736](https://github.com/Connextstrategy/Electric-Vehicles-In-Washington-State/assets/18508699/6eae65c5-3353-497c-a92f-e934a5652fab)

  ![Screenshot 2023-10-19 133838](https://github.com/Connextstrategy/Electric-Vehicles-In-Washington-State/assets/18508699/43769b4a-f19d-4f4b-9cdc-c22a9a1082e7)




### Dependencies

* Using Visual Studio Code for coding and data visualizations
* Web browser to show data visualizations (Google Chrome used but coudl be Mozilla or another)
* Use index to initiate data visualization
* Use app file in static folder to understand code for application

### Installing

* No modifications needed to be made to files/folders

## Help

* Use console.log inside of your JavaScript code to see what your data looks like at each step.

* Refer to the Plotly.js documentationLinks to an external site. when building the plots.

## Authors

Christopher Manfredi

## Version History

    * Initial Release

## Acknowledgments

* This is specifically for an exercise for Rutgers Boot Camp 
