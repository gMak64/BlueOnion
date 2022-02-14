CREATE DATABASE IF NOT EXISTS test;

use test;

CREATE TABLE IF NOT EXISTS satellite_locations(
	satellite_id VARCHAR(40) NOT NULL,
	latitude FLOAT,
	longitude FLOAT,
	create_date DATETIME,
	PRIMARY KEY (satellite_id, create_date)
);
