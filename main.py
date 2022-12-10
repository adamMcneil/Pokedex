import fileinput
from multiprocessing.connection import Connection
from sql_server import create_server_connection, make_sql_query

# INSERT INTO `pokemon` (name, pokedex_number, hp, attack, special_attack, defence, special_defence, speed, ability1)
# VALUES('mew', 151, 1, 1, 1, 1, 1, 1, 'transform')
# pokedex_number, name, base_stat, hp, attack, special_attack, defence, special_defence, speed, generation, isLegendary


def add_pokemon(connection: Connection) -> None:

    database = "`pokemon`"
    column_order = "(pokedex_number, name, type_1, type_2, base_stat, hp, attack, special_attack, defence, special_defence, speed, generation, isLegendary)"

    for line in fileinput.input(files="sql_pokemon.csv"):
        query = "INSERT INTO " + database + " " + \
            column_order + " VALUES (" + line + ");"
        # print(query)
        make_sql_query(connection, query)


# it is the password you set up when you install mysql
password = "Pokemon2022!"
# database you want to use
database = "pokedex"

query = "select * from pokemon where base_stat < 200 order by base_stat;"

# connect to the server
connection = create_server_connection("localhost", "root", password)

# specify you are using the pokedex database on the server
make_sql_query(connection, "USE " + database)
add_pokemon(connection)
# then store the results of the query in result and print the list, results.
results = make_sql_query(connection, query)
for result in results:
    print(result)
