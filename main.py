import fileinput
from multiprocessing.connection import Connection
from sql_server import create_server_connection, make_sql_query
from fill_tables import insert_all_tables


# it is the password you set up when you install mysql
password = "Pokemon2022!"
# database you want to use
database = "pokedex"
query = "select * from pokemon;"
connection = create_server_connection("localhost", "root", password)
# specify you are using the pokedex database on the server
make_sql_query(connection, "USE " + database)

insert_all_tables(connection, database, password)


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


# connect to the server


# then store the results of the query in result and print the list, results.
#results = make_sql_query(connection, get_all_pokemon_from_generation)


# prints results from the given query
def printRes(results):
    for result in results:
        print(result)


# main code loop
running = True
print("Welcome to the Ultimate Pokedex, Trainer!")
while (running == True):
    userChoice = input('''
    Search Pokemon by:
        1. Name
        2. Number
        3. Type
        4. Generation
        5. SQL Query Input
        6. Moveset
        7. Quit
    ''')
    if (userChoice == "1"):
        nameSearch = input("Enter a Pokemon name to search for: ")
        # check this query
        getName = f"select *\
                    from pokemon \
                    where name = '{nameSearch}'"

        results = make_sql_query(connection, getName)
        if (results):
            printRes(results)
        else:
            print("No Pokemon with that name.")

            # DONE

    elif (userChoice == "2"):
        numSearch = input("Enter a Pokemon number to search for: ")
        # check this query
        getName = f"select *\
                    from pokemon \
                    where pokedex_number = {numSearch}"
        results = make_sql_query(connection, getName)
        if (results):
            printRes(results)
        else:
            print("No Pokemon with that number.")
            # DONE

    elif (userChoice == "3"):
        typeSearch = input("Enter a type to search for Pokemon of that type: ")
        getName = f"select * \
                    from pokemon \
                    where type_1 = '{typeSearch}' OR type_2 = '{typeSearch}'"

        results = make_sql_query(connection, getName)
        if (results):
            printRes(results)
        else:
            print("No Pokemon with that type.")
            # DONE

    elif (userChoice == "4"):
        genSearch = input(
            "Enter a type to search for Pokemon from that game generation: ")
        get_all_pokemon_from_generation = f"select * \
                                    from pokemon \
                                    where generation = {genSearch}"

        results = make_sql_query(connection, get_all_pokemon_from_generation)
        if (results):
            printRes(results)
        else:
            print("No Pokemon from that Generation.")
            # DONE

    elif (userChoice == "5"):
        query = input("Enter a sql query: ")

        results = make_sql_query(connection, query)
        if (results):
            printRes(results)
        else:
            print("No results.")
            # DONE

    elif (userChoice == "6"):
        moveSearch = "\'" + \
            input("Enter a move to seach for: ") + "\'"
        get_all_pokemon_know_move = f"select * \
                            from pokemon inner join level_moves on pokemon.pokedex_number=level_moves.pokemon_number \
                            where move = {moveSearch}"

        results = make_sql_query(connection, get_all_pokemon_know_move)
        if (results):
            printRes(results)
        else:
            print("No pokemon knows that move.")
            # DONE

    elif (userChoice == "7"):
        running = False
        break
    else:
        print("Invalid choice. Please choose a valid option!")
