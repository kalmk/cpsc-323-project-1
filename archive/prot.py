def read_input():
    file = open("input.in", "r")
    list_of_lines = file.readlines()

    return list_of_lines

def go_char_by_char(line):
    for char in line:
        print(char)

