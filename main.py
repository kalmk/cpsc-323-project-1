from scan_lines import *
from change_state import *
from get_token import *
from dfa import *
from tokenizer import *

def main():
    token_stream = ""
    chars_scanned = ""

    # Current state can be derived by rows (meaning state) and columns (meaning input), q0 = row 0
    current_row = 0
    current_column = 0
    token = ""

    # to access dfa table, use dfa.dfa_table

    input_lines = scan_lines("input.in")
    # print(input_lines)

    while (True):
        # Go line by line
        for line in input_lines:

            for char in line:
                # Now we are reading each character in each line one by one
                if (char == "\n"):
                    continue

                
                reject = False
                # call function to change state according to input
                # Ex. reject, curret_row, current_column = change_state(char, current_row, current_column)
                list1 = change_state(char, current_row, current_column)

                reject = list1[0]
                current_row = list1[1]
                current_column = list1[2]

                # print(reject, current_row)

                if (reject):
                    # First, get back the appropriate token for chars_scanned
                    if ((chars_scanned == " ") or (chars_scanned == "")):
                        continue
                    token = get_token(current_row)
                    is_keyword = get_keyword(chars_scanned)
                    print(f"keyword: {is_keyword}")
                    if is_keyword != "IDENTIFIER":
                        token = is_keyword
                    token_stream = token_stream + " " + token
                    print(f"For chars '{chars_scanned}', saved '{token}' to the token stream")

                    token = ""
                    chars_scanned = ""

                    current_row = 0

                    list1 = change_state(char, current_row, current_column)

                    reject = list1[0]
                    current_row = list1[1]
                    current_column = list1[2]

                # If our dfa didn't reject, append the char
                chars_scanned += char
                chars_scanned = chars_scanned.strip()

                # print(char)
        
        break

    # After finishing scanning all characters, check if there's an unsaved token
    if chars_scanned:
        token = get_token(int(current_row))

        is_keyword = get_keyword(chars_scanned)
        if is_keyword != "IDENTIFIER":
            token = is_keyword
        token_stream = token_stream + " " + token
        # print(f"For chars '{chars_scanned}', saved '{token}' to the token stream")   

    print("Token stream:", token_stream)

if __name__ == "__main__":
    main()