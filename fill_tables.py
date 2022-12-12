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


def insert_all_tables(connection: Connection, database: str, password: str) -> None:
    # pokemon data fro insert
    pokemon_csv_file = "csv_files/sql_pokemon.csv"
    pokemon_table = "pokemon"
    pokemon_column_order = "(pokedex_number, name, type_1, type_2, base_stat, hp, attack, special_attack, defence, special_defence, speed, generation, isLegendary)"

    # move data for insert
    move_csv_file = "csv_files/sql_good_move.csv"
    move_table = "moves"
    move_column_order = "(name, type, category, description, power, accury, pp, tm_number, probability, generation)"

    # data for pokemon and move data
    learn_csv_file = "csv_files/sql_pokemon_move.csv"
    learn_table = "level_moves"
    learn_column_order = "(pokemon_number, move)"

    # data for generations and region names
    generation_csv_file = "csv_files/sql_generation.csv"
    generation_table = "generations"
    generation_column_order = "(number,name)"

    # specify you are using the pokedex database on the server

    make_sql_query(connection, "USE " + database)

    insert_csv_file(connection, generation_csv_file,
                    generation_table, generation_column_order)
    print("Added all of the genrations")

    insert_csv_file(connection, pokemon_csv_file,
                    pokemon_table, pokemon_column_order)
    print("Added all of the pokemon")

    insert_csv_file(connection, move_csv_file,
                    move_table, move_column_order)
    print("Added all of the moves")

    insert_csv_file(connection, learn_csv_file,
                    learn_table, learn_column_order)
    print("Added all of the move that a Pokemon could learn")
