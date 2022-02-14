import mysql.connector
import json
from datetime import datetime


def load_data():
    con = mysql.connector.connect(
        host="127.0.0.1",
        user="user",
        password="password",
        database="test"
    )
    cur = con.cursor()

    sql = """INSERT INTO satellite_locations (satellite_id, latitude, longitude, create_date) 
                    VALUES 
                        (%s, %s, %s, %s) 
                    ON DUPLICATE KEY UPDATE 
                        latitude = VALUES(latitude),
                        longitude = VALUES(longitude)"""
    data = read_json()

    start = datetime.now()
    cur.executemany(sql, data)
    con.commit()
    end = datetime.now()

    data_size = str(len(data))
    exec_time = str(end - start)
    print(data_size + " entries loaded in " + exec_time + " seconds.")


def read_json():
    insert_data = []
    with open('./starlink_historical_data.json') as json_file:
        data = json.load(json_file)
        for i in data:
            sat_id = i['id']
            latitude = i['latitude']
            longitude = i['longitude']
            create_date = i['spaceTrack']['CREATION_DATE']
            if latitude is not None and longitude is not None:
                insert_data.append((sat_id, latitude, longitude, create_date))

    return insert_data


if __name__ == '__main__':
    load_data()
