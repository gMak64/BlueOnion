# Blue Onion Take Home Assignment
Author: Grant Mak
Email: gmak6464@gmail.com
## Task 1
To standup the db, run `docker-compose up` in the main directory. This will create a connection on `127:0.0.:3306`. If you are running a MacBook with an M1 Chip, you may need to run `docker pull --platform linux/x86_64 mysql`.

## Task 2
The Python script  `load_data.py` handles this task. Once the database from **Task 1** is up and running, this can be run to load the satellite data into that database. Once run, it will output the time taken to load the file, which took around 0.33 seconds on average on my local machine.

This assumes that the JSON file remains in the same directory as the script, and that you have `mysql-connector-python` imported.

## Task 3
```
use test;

SELECT sl1.satellite_id, sl1.latitude, sl1.longitude, sl1.create_date
FROM satellite_locations sl1
RIGHT JOIN
	(
		SELECT satellite_id, MAX(create_date) as closest_date
        FROM satellite_locations 
        WHERE satellite_id = ID
		AND create_date <= T
        GROUP BY satellite_id
    ) AS sl2
ON sl1.satellite_id = sl2.satellite_id AND sl1.create_date = sl2.closest_date;
```

## Task 4
The Python script  `closest_sat.py` handles this task. Once the database from **Task 1** is up and running, this can be used to query for the given task. It will ask you for an ISO formatted timestamp, a latitude, and a longtitude. Once you provide 3 valid parameters, it will return the closest satellite.

This assumes that the script from **Task 2** has been used to load the database, and that you have `haversine` imported.
