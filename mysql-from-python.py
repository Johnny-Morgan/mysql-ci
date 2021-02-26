import os
import datetime
import pymysql

username = os.getenv('gitpod')

# Connect to database
connection = pymysql.connect(host='localhost',
                             user=username,
                             password='',
                             db='Chinook')

try:
    # Run query
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        rows = [("John", 56, "1955-05-09 13:12:45"),
                ("Jack", 38, "1982-09-02 01:44:56"),
                ("Hurley", 27, "1993-01-23 04:07:12"),
                ("Kate", 29, "1991-12-11 22:11:13"),
                ("Sawyer", 38, "1982-10-10 07:34:21"),
                ("Jin", 41, "1979-03-30 18:05:06")]

        cursor.executemany('INSERT INTO Friends VALUES (%s, %s, %s);', rows)
        connection.commit()
finally:
    # Close connection
    connection.close()
