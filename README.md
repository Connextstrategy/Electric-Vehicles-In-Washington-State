## Python Rutgers Bootcamp Challenge "Project Three"  - Electric Vehicles In State of Washington

This activity is broken down into multiple deliverables which makes progress towards developing a full-stack data visualization web application that allows users to interactively explore a dataset.

## Description

In this assignment, we will need to complete the following objectives: 

**Data and Delivery**

* Data components used in the project are clearly documented. 
* The dataset contains at least 100 unique records. 
* A database is used to house the data (SQL, MongoDB, SQLite, etc.). 
* The project is powered by a Python Flask API and includes HTML/CSS, JavaScript, and the chosen database
  
**Back End**

* The page created to showcase data visualizations runs without error. 
* A JavaScript library not shown in class is used in the project. 

**The project conforms to one of the following designs**

* A Leaflet or Plotly chart built from data gathered through web scraping.
* A dashboard page with multiple charts that all reference the same data.
  
**Visualizations** 

* A minimum of three unique views present the data. 
* Multiple user-driven interactions (such as dropdowns, filters, or a zoom feature) are included on the final page. 
* The final page displays visualizations in a clear, digestable manner. 
* The data story is easy to interpret for users of all levels.
  
## Instructions

1. **Identifying Data For Analysis**

* Our group chose to select and analyze data based on  [Electric Vehicle Population Data](https://data.wa.gov/Transportation/Electric-Vehicle-Population-Data/f6w7-q2d2).

![Screenshot 2023-10-19 123414](https://github.com/Connextstrategy/Electric-Vehicles-In-Washington-State/assets/18508699/85ac7034-ca05-4c0e-b3b7-2077f3790f5a)

* This data was important as it included numerous data types to be used for visualizations in the project to include Make, Model, County, City, State, Postal Code, Electric Vehicle and EV Type

![Screenshot 2023-10-19 123431](https://github.com/Connextstrategy/Electric-Vehicles-In-Washington-State/assets/18508699/065bfd2e-dbe4-4ede-9714-98fa7e8ebbd5)

* We wanted to include data which included data on prices, range of vehicles and charge rates, so we identified [this website](https://ev-database.org)

* This enabled us to pull important data (MSRP, RapidCharge, Range, etc.) based on the previous State of Washington electric vehicles model names

![Screenshot 2023-10-19 131057](https://github.com/Connextstrategy/Electric-Vehicles-In-Washington-State/assets/18508699/6b216ab6-7fb5-427f-a708-a64aff0ad184)

2. **Webscraping EV Database And Exporting CSV File For Integrated Database Creation**

* In order to get the data from the EV database website, we we forced to scrap the data from it via Beautiful Soup in Python and then create a dataframe off the data pulled to include the data we required for our visualizations

![Screenshot 2023-10-19 131311](https://github.com/Connextstrategy/Electric-Vehicles-In-Washington-State/assets/18508699/5fb9a08c-af9e-4228-9beb-a6b92c03e307)

![Screenshot 2023-10-19 131335](https://github.com/Connextstrategy/Electric-Vehicles-In-Washington-State/assets/18508699/052b1b48-3723-4f9b-9fb8-6b6e37d1c597)

* Following the dataframe creation we exported a clean CSV file named EV_Analysis_Database
  
* Python file can be found [here](https://github.com/Connextstrategy/Electric-Vehicles-In-Washington-State/tree/main/python_files) and CSV file can be found [here](https://github.com/Connextstrategy/Electric-Vehicles-In-Washington-State/tree/main/cleaned_csv_files)
  
3. **Cleaning up Electric Vehicle Population Data For Exporting CSV File For Integrated Database Creation**

* We need to clean up the data for the Electric Vehicle Population data from State of Washington so we did the following:
  - Dropped NAs
  - Removed years older than 2022
  - Extracted longitude and latitude data from Vehicle Location variable
  - Dropped columns not neccesary from analysis
  - Removed or extracted only models we deemed necessary for analysis
  - Matched correct Model Names with the same exact syntax from the EV_Analysis_Database
 
  ![Screenshot 2023-10-19 133736](https://github.com/Connextstrategy/Electric-Vehicles-In-Washington-State/assets/18508699/6eae65c5-3353-497c-a92f-e934a5652fab)

  ![Screenshot 2023-10-19 133838](https://github.com/Connextstrategy/Electric-Vehicles-In-Washington-State/assets/18508699/43769b4a-f19d-4f4b-9cdc-c22a9a1082e7)

* Following our cleaning, we exported a clean csv file named EV_WA_cleaned
  
* Python file can be found [here](https://github.com/Connextstrategy/Electric-Vehicles-In-Washington-State/tree/main/python_files) and CSV file can be found [here](https://github.com/Connextstrategy/Electric-Vehicles-In-Washington-State/tree/main/cleaned_csv_files)

4. **Quick Database Diagramming & Uploading files to Post GRES for Database Creation**

 * We drew up a [Quick Database Diagram](https://app.quickdatabasediagrams.com/#/) to sketch out the schema for our data

![Screenshot 2023-10-24 153524](https://github.com/Connextstrategy/Electric-Vehicles-In-Washington-State/assets/18508699/696d1456-2cb1-4110-a8e7-984c8e28e06f)

 * We then needed to create one database for our files, so we created one via pgAdmin

![Screenshot 2023-10-19 135100](https://github.com/Connextstrategy/Electric-Vehicles-In-Washington-State/assets/18508699/eabe8e75-e891-4282-a512-96934521664d)

5. **Flask Creation For SQL Connection And JSON Creation For Data Visualization**

* Import multiple specific libraries for running Flask application
* Ensure you create take buitl SQL library and connect it via code for engine (see below)
* **Note use "postgres" = Log In User Name for PgAdmin**
* **Note use "password" = Password for PgAdmin**

![Screenshot 2023-10-24 155528](https://github.com/Connextstrategy/Electric-Vehicles-In-Washington-State/assets/18508699/2f0bdc32-9f2c-4596-bb88-acac2129219a)

* Query both sets of data from both tables (we did not do Left Join in SQL but this is optional)
* Build dictionaries for large json file creation

![Screenshot 2023-10-24 160150](https://github.com/Connextstrategy/Electric-Vehicles-In-Washington-State/assets/18508699/74897227-107f-4a22-af2c-0bf7453e1d11)

* We built multiple json files to be exported for multiple types of analysis (not all were used)

![Screenshot 2023-10-24 160514](https://github.com/Connextstrategy/Electric-Vehicles-In-Washington-State/assets/18508699/44581945-6ef3-4002-857b-c64822dcdf60)

  6. **Plots.js Creation For Data Visualizations**

* Included [Circletype.js](https://circletype.labwire.ca/) for text changes in HTML
* Used OptionsChanged functions to add d3.js functionality
* Created and made layout changes for three different charts to include a pie, bar, and gauge chart

![Screenshot 2023-10-24 160755](https://github.com/Connextstrategy/Electric-Vehicles-In-Washington-State/assets/18508699/9202fe96-a15a-4e21-ad6f-8f5e587522c4)

  7. **Home HTML Creation**

* Added onchange selection tool for data selection fields (1 for Model and 2 for Make)
* Imported CircleType.js, Vanta.js, Plotly, and d3js
* Attributes plots.js file to HTML creation

![Screenshot 2023-10-24 162103](https://github.com/Connextstrategy/Electric-Vehicles-In-Washington-State/assets/18508699/76426081-af79-4726-9f88-93850e00d342)

  
### Dependencies

* Using Visual Studio Code for coding and data visualizations
* Web browser to show data visualizations (Google Chrome used but coudl be Mozilla or another)
* Use index to initiate data visualization
* Use app file in static folder to understand code for application
  
- Imports For Flask Application 
* from types import prepare_class
* import numpy as np
* import pandas as pd
* import sqlalchemy
* from sqlalchemy.ext.automap import automap_base
* from sqlalchemy.orm import Session
* from sqlalchemy import create_engine, func
* from flask import Flask, render_template
* import json
* import psycopg2
* from flask import Flask, jsonify

Javscript Libraries Used
* [CircleType](https://circletype.labwire.ca/) for curved text
* [Vanta.js](https://www.vantajs.com/?effect=fog) for fog background

### Installing

* Open Gitbash terminal inside Project Folder which include the following:
- Home
- app_EV_Anlaysis_Full
- plots.js

1. Type in "conda activate dev" into Gitbash
2. Type "python -m app_EV_Analysis_Full into Gitbash

![Screenshot 2023-10-24 161144](https://github.com/Connextstrategy/Electric-Vehicles-In-Washington-State/assets/18508699/9631e861-5906-47d3-ac8d-faa1fb018d62)

* Ensure you are building your own PostgreSQL file. Have log in and password and put it into 

## Help

* Use console.log inside of your JavaScript code to see what your data looks like at each step.

* Refer to the Plotly.js documentationLinks to an external site. when building the plots.

## Authors

Christopher Manfredi, Brandon Mata Chacon, Paul Boerstel, Vignesh Cheirath, Allison Potestio, Spencer Auslander

## Version History

    * Initial Release

## Acknowledgments

* This is specifically for an exercise for Rutgers Boot Camp 
