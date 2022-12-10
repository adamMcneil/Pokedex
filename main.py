
from multiprocessing.connection import Connection
import mysql.connector
from mysql.connector import Error
# import pandas as pd


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


def make_sql_request(connection: Connection, query: str):
    cursor = connection.cursor()
    try:
        cursor.execute("use pokedex")
        cursor.execute(query)
        result = cursor.fetchall()
        print("query successful")
        return result
    except Error as err:
        print(f"error: '{err}'")
    return


pw = "Pokemon2022!"

db = "pokedex"

query = "select * from pokemon;"


connection = create_server_connection("localhost", "root", pw)

cursor = connection.cursor()
cursor.execute("use pokedex")

result = make_sql_request(connection, query)
print(result)
