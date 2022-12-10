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


# it is the password you set up when you install mysql
password = "Pokemon2022!"
# database you want to use
database = "pokedex"

query = "select * from pokemon where overall_stat < 200 order by overall_stat;"

# connect to the server
connection = create_server_connection("localhost", "root", password)

# specify you are using the pokedex database on the server
make_sql_query(connection, "USE " + database)

# then store the results of the query in result and print the list, results.
results = make_sql_query(connection, query)
for result in results:
    print(result)
