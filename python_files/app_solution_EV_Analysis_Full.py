from types import prepare_class
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, render_template
import json
import psycopg2


from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("postgresql+psycopg2://postgres:Tgyhu10#@localhost:5432/EV_Database")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Save reference to the table(s)
EV_WA_Vehicles = Base.classes.ev_washington
EV_Analysis_Database = Base.classes.ev_vehicle_database

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/extract"
    )


@app.route("/extract")
def extract():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of passenger data including the name, age, and sex of each passenger""",

    # Query all data from both tables 
    results = session.query(EV_WA_Vehicles.make, EV_WA_Vehicles.model, EV_WA_Vehicles.model_year,
                            EV_WA_Vehicles.county, EV_WA_Vehicles.city, EV_WA_Vehicles.postal_code, EV_WA_Vehicles.electric_vehicle_type, 
                            EV_WA_Vehicles.cafv_eligibility, EV_WA_Vehicles.longitude, EV_WA_Vehicles.latitude).all()
                         
    results2 = session.query(EV_Analysis_Database.model, EV_Analysis_Database.msrp, EV_Analysis_Database.pricerange,
                            EV_Analysis_Database.efficiency, EV_Analysis_Database.rapidcharge, EV_Analysis_Database.range).all()

    session.close()

    # Create a dictionary from the row data and append to a list of all_passengers
    all_EV_data = []
    for Make, Model, Model_Year, County, City, Postal_Code, Electric_Vehicle_Type, CAFV_Eligibility, longitude, latitude,   in results:
        EV_data_dict = {}
        EV_data_dict["Make"] = Make
        EV_data_dict["Model"] = Model
        EV_data_dict["Year"] = Model_Year
        EV_data_dict["Longitude"] = float(longitude)
        EV_data_dict["Latitude"] = float(latitude)
        EV_data_dict["County"] = County
        EV_data_dict["City"] = City
        EV_data_dict["Zip Code"] = Postal_Code
        EV_data_dict["Vehicle Type"] = Electric_Vehicle_Type
        EV_data_dict["CAFV Eligibility"] = CAFV_Eligibility
        all_EV_data.append(EV_data_dict)
    EV_data_df = pd.DataFrame(all_EV_data)
    
    # new info for second visualization
    ev_database_data = []
    for model, msrp, pricerange, efficiency, rapidcharge, range, in results2:
        EV_database_dict = {}
        EV_database_dict["Model"] = model
        EV_database_dict["Msrp"] = msrp
        EV_database_dict["PriceRange"] = pricerange
        EV_database_dict["Efficiency"] = efficiency
        EV_database_dict["Rapidcharge"] = rapidcharge
        EV_database_dict["Range"] = range
        ev_database_data.append(EV_database_dict)
    database_df=pd.DataFrame(ev_database_data)

    merged_df = EV_data_df.merge(database_df, on = "Model")
    temp = merged_df.value_counts("Model")
    temp.name = "count"
    merged_df = merged_df.merge(temp, on="Model")
    grouped_df=merged_df.groupby("Model")
    groupdict = {}
    for column in grouped_df.head(1).columns:
        groupdict[column] = (grouped_df.head(1)[column].tolist())

    test = open('static/merged_json.json', 'w')
    test.write(json.dumps(merged_df.to_dict('records')))
    test.close

    test2 = open('static/grouped_json.json', 'w')
    test2.write(json.dumps(groupdict))
    test2.close

    file2 = open('static/all_EV_WA_data_JSON.json', 'w')
    file2.write(json.dumps(all_EV_data))
    file2.close

    modellist = [a['Model'] for a in all_EV_data]
    countylist = [a['County'] for a in all_EV_data]
    Model_dict = {
    "modelind":list(pd.Series(modellist).unique()),
    "modelvc" :list(pd.Series(modellist).value_counts()),
    "county" :list(pd.Series(countylist).unique())
    }

    file4 = open('static/model_JSON.json', 'w')
    file4.write(json.dumps(Model_dict))
    file4.close

#second visualization test

    file3 = open('static/ev_database_data_JSON.json', 'w')
    file3.write(json.dumps(ev_database_data))
    file3.close

    modellist2 = [a['Model'] for a in all_EV_data]
    modellist3 = [a['Msrp'] for a in ev_database_data]
    modellist4 = [a['Range'] for a in ev_database_data]
    MSRP_dict = {
    "modelind":list(pd.Series(modellist2).unique()),
    "modelvc" :list(pd.Series(modellist3)),
    "range":list(pd.Series(modellist4))
    }

    file5 = open('static/model2_JSON.json', 'w')
    file5.write(json.dumps(MSRP_dict))
    file5.close

## third visualization

    modellist4 = [a['Range'] for a in ev_database_data]
    MSRP_dict = {
    "modelind":list(pd.Series(modellist2).unique()),
    "modelvc" :list(pd.Series(modellist4))
    }

    file6 = open('static/model3_JSON.json', 'w')
    file6.write(json.dumps(MSRP_dict))
    file6.close

    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)

