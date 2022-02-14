import mysql.connector
from haversine import haversine
import datetime


def get_closest(time, lat, long):
    con = mysql.connector.connect(
        host="127.0.0.1",
        user="user",
        password="password",
        database="test"
    )
    cur = con.cursor()

    sql = """SELECT satellite_id, latitude, longitude 
             FROM satellite_locations 
             WHERE create_date = %s""";

    cur.execute(sql, (time,))
    res = cur.fetchall()

    closest_id = ""
    closest_distance = float('inf')
    lat_long = (lat, long)
    for i in res:
        loc = i[1:]
        dist = haversine(lat_long, loc)
        if dist < closest_distance:
            closest_distance = dist
            closest_id = i[0]
    print(closest_id)


if __name__ == '__main__':
    invalid_time = True
    invalid_lat = True;
    invalid_long = True;

    time_in = input("Enter a UTC time in form 'YYYY-MM-DDThh:mm:ss': ")
    while invalid_time:
        try:
            time_in = datetime.datetime.strptime(time_in, "%Y-%m-%dT%H:%M:%S")
            invalid_time = False
        except ValueError:
            time_in = input("Your input was not in YYYY-MM-DDThh:mm:ss format. Please try again: ")

    lat_in = input("Enter a latitude: ")
    while invalid_lat:
        try:
            lat_in = float(lat_in)
            invalid_lat = False
        except ValueError:
            lat_in = input("Please input a valid number: ")

    long_in = input("Enter a longitude: ")
    while invalid_long:
        try:
            long_in = float(long_in)
            invalid_long = False
        except ValueError:
            long_in = input("Please input a valid number: ")

    get_closest(time_in, lat_in, long_in)
