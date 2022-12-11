import fileinput
from multiprocessing.connection import Connection
from sql_server import create_server_connection, make_sql_query
from fill_tables import insert_all_tables


# it is the password you set up when you install mysql
password = "Pokemon2022!"
# database you want to use
database = "pokedex"
query = "select * from pokemon;"

# gets all pokemon and all their moves
get_pokemon_moves = "select pokemon.pokedex_number, pokemon.name, level_moves.move \
                    from pokemon inner join level_moves on pokemon.pokedex_number=level_moves.pokemon_number"

# gets all moves of a pokemon name
get_single_pokemon_moves = "select pokemon.pokedex_number, pokemon.name, level_moves.move \
                            from pokemon inner join level_moves on pokemon.pokedex_number=level_moves.pokemon_number \
                            where pokemon.pokedex_number = 4"

# get all pokemon that know certain move
get_all_pokemon_know_move = "select pokemon.pokedex_number, pokemon.name, level_moves.move \
                            from pokemon inner join level_moves on pokemon.pokedex_number=level_moves.pokemon_number \
                            where move = \'Heat Crash\'"

# get all pokemon from a generation
get_all_pokemon_from_generation = "select * \
                                    from pokemon \
                                    where generation = 2"

# connect to the server
connection = create_server_connection("localhost", "root", password)

# specify you are using the pokedex database on the server
make_sql_query(connection, "USE " + database)

insert_all_tables(connection, database, password)

# then store the results of the query in result and print the list, results.
results = make_sql_query(connection, get_all_pokemon_from_generation)
for result in results:
    print(result)
