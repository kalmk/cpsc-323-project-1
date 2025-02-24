def read_input():
    file = open("input.in", "r")
    list_of_lines = file.readlines()
    
    return list_of_lines

def go_char_by_char(line_number):
    file = open("input.in", "r")
    lines = file.readlines()

    for line in lines:
        print(line)
        for char in line:
            print(char)

