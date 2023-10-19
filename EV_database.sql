DROP TABLE IF EXISTS EV_Washington;
DROP TABLE IF EXISTS EV_Vehicle_Database;

CREATE TABLE EV_Vehicle_Database (
	Model VARCHAR PRIMARY KEY,
	PriceRange INT,
	Efficiency INT,
	Rapidcharge INT,
	Range INT,
	MSRP INT
);

CREATE TABLE EV_Washington (
	ids INT PRIMARY KEY,
	VIN VARCHAR NOT NULL,
	County VARCHAR NOT NULL,
	City VARCHAR NOT NULL,
	Postal_Code INT NOT NULL,
	Model_Year INT NOT NULL,
	Make VARCHAR NOT NULL,
	Model VARCHAR NOT NULL,
	FOREIGN KEY (Model) REFERENCES EV_Vehicle_Database(Model),
	Electric_Vehicle_Type VARCHAR NOT NULL,
	CAFV_Eligibility VARCHAR NOT NULL,
	Longitude NUMERIC,
	Latitude NUMERIC
);

SELECT * FROM EV_Vehicle_Database;
SELECT * FROM ev_washington;