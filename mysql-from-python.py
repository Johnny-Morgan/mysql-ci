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
        cursor.execute(
            '''CREATE TABLE IF NOT EXISTS
            Friends(name char(20), age int, DOB datetime);''')
finally:
    # Close connection
    connection.close()
