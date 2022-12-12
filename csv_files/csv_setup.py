def add_quotes(file_name: str, string_indecies: list) -> None:
    original = open(file_name, "r")
    new = open("sql_" + file_name, "w")
    for line in original:
        line = line.replace("\n", "")
        line_list = line.split(',')
        for i in string_indecies:
            line_list[i] = "\'" + line_list[i] + "\'"
        line = ','.join(str(item) for item in line_list)
        new.write(line + "\n")

#
# This script is used to convert csv files to a better format so they can easily be used with a sql query
#


def remove_bad_rows(file_name: str) -> None:
    original = open(file_name, "r")
    new = open("good_" + file_name, "w")
    for line in original:
        count = 0
        for x in line:
            if x == ',':
                count += 1
            if x == '\'':
                count = 10
        if count == 9:
            new.write(line)


remove_bad_rows("move.csv")

add_quotes("pokemon.csv", [1, 2, 3, 12])
# add_quotes("good_move.csv", [0, 1, 2, 3])
add_quotes("pokemon_move.csv", [1])
