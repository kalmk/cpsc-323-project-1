from scan_lines import *


def main():
    token_stream = ""
    chars_scanned = ""

    # Call function to make a copy of our DFA here
    # Ex. our_dfa = make_dfa()

    # Current state can be derived by rows and columns, q0 = row 0
    current_row = 0
    current_column = 0
    token = ""

    input_lines = scan_lines("input.in")
    # print(input_lines)

    while (True):
        # Go line by line
        for line in input_lines:

            for char in line:
                # Now we are reading each character in each line one by one
                if ((char == "\n") or (char == " ")):
                    continue
                
                reject = False
                # call function to change state according to input
                # Ex. reject, curret_row, current_column = change_state(char, current_row, current_column)



                if (reject):
                    # First, get back the appropriate token for chars_scanned
                    # Ex. token = get_token(current_row, current_column)
                    token_stream += token

                    token = ""
                    chars_scanned = ""
                    continue

                # If our dfa didn't reject, append the char
                chars_scanned += char

                print(char)

        
        break

if __name__ == "__main__":
    main()