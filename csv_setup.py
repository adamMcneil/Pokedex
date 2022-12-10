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


add_quotes("pokemon.csv", [1, 2, 3, 12])
