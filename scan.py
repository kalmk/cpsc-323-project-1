from regex import *

def scan_code():
    file = open("input.in", "r")
    lines = file.readlines()

    tokens = []
    word = ""
    
    for char in lines:
        char = char.split()
        for c in char :
            for x in c:
                print(x)
                if x.isalnum():
                    word += x
                    # implement recognize keywords here such as int or main
                else:
                    if identifer_regex(word):
                        tokens.append("identifier")
                    elif number_regex(word):
                        tokens.append("number")
                    word = ""

                if x in ('(', ')'): # for testing purpose
                    tokens.append("hurray")

    if word:
        if identifer_regex(word):
                tokens.append("identifier")
        elif number_regex(word):
            tokens.append("number")

    return tokens
