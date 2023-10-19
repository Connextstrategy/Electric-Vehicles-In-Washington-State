## Python Rutgers Bootcamp Challenge - Electric Vehicles In State of Washington

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

* We wanted to include data which included data on prices, range of vehicles and charge rates, so we identified [https://ev-database.org/uk/compare/newest-upcoming-electric-vehicle#sort:path~type~order=.id~number~desc|range-slider-range:prev~next=0~600|range-slider-towweight:prev~next=0~2500|range-slider-acceleration:prev~next=2~23|range-slider-fastcharge:prev~next=0~1100|range-slider-eff:prev~next=150~500|range-slider-topspeed:prev~next=60~260|paging:currentPage=0|paging:number=all](https://ev-database.org/#sort:path~type~order=.rank~number~desc|range-slider-range:prev~next=0~1200|range-slider-acceleration:prev~next=2~23|range-slider-topspeed:prev~next=110~350|range-slider-battery:prev~next=10~200|range-slider-towweight:prev~next=0~2500|range-slider-fastcharge:prev~next=0~1500|paging:currentPage=0|paging:number=9)

  ![Screenshot 2023-10-10 135515](https://github.com/Connextstrategy/belly-button-challenge/assets/18508699/c6518639-4f51-479c-846b-9ab7704f41a8)




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
