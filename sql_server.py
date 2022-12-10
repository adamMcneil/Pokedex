from multiprocessing.connection import Connection
import mysql.connector
from mysql.connector import Error

# connects to the server and returns the connection for later queries


def create_server_connection(host_name, user_name, user_password) -> Connection:
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("mysql database connection successful")
    except Error as err:
        print(f"error: '{err}'")
    return connection

# use this to get the results of sql query return as a list where query is just a string like a normal sql query


def make_sql_query(connection: Connection, query: str):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        print("query successful")
        return result
    except Error as err:
        print(f"error: '{err}'")
    return
