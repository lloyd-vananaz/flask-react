import mysql.connector 
from mysql.connector import Error

try:
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='password',
        database='database_name'
    )
    cursor = connection.cursor()
    cursor.execute("select database();")
    record = cursor.fetchone()
    print("You're connected to database: ", record)
except Error as e:
    print('Error', e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print('Disconnected')