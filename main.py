import fileinput
from multiprocessing.connection import Connection
from sql_server import create_server_connection, make_sql_query

# INSERT INTO `pokemon` (name, pokedex_number, hp, attack, special_attack, defence, special_defence, speed, ability1)
# VALUES('mew', 151, 1, 1, 1, 1, 1, 1, 'transform')
# pokedex_number, name, base_stat, hp, attack, special_attack, defence, special_defence, speed, generation, isLegendary


def insert_csv_file(connection: Connection, csv_file: str, table: str, column_order: str) -> None:
    for line in fileinput.input(files=csv_file):
        query = "INSERT INTO `" + table + "` " + \
            column_order + " VALUES (" + line + ");"
        # print(query)
        make_sql_query(connection, query)


# pokemon data fro insert
pokemon_csv_file = "sql_pokemon.csv"
pokemon_table = "pokemon"
pokemon_column_order = "(pokedex_number, name, type_1, type_2, base_stat, hp, attack, special_attack, defence, special_defence, speed, generation, isLegendary)"

# move data for insert
move_csv_file = "sql_move.csv"
move_table = "moves"
move_column_order = "(name, type, category, description, power, accury, pp, tm_number, probability, generation)"

# it is the password you set up when you install mysql
password = "Pokemon2022!"
# database you want to use
database = "pokedex"
query = "select * from moves;"


# connect to the server
connection = create_server_connection("localhost", "root", password)

# specify you are using the pokedex database on the server
make_sql_query(connection, "USE " + database)


insert_csv_file(connection, pokemon_csv_file,
                pokemon_table, pokemon_column_order)
insert_csv_file(connection, move_csv_file,
                move_table, move_column_order)

# then store the results of the query in result and print the list, results.
results = make_sql_query(connection, query)
for result in results:
    print(result)
