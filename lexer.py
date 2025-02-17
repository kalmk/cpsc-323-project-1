# All keywords are their own token, so their
# corresponding output token is the same as the lexeme
keywords = ["int", "return", "if", "switch", "float", "while", "else", "case",
            "char", "for", "goto", "unsigned", "main", "break", "continue", "void"]

operators = ["(", ")", "[", "]", "{", "}", ".", "+", "-", "*", "/", "%", "<",
             ">", "=", ";", ",", "++", "--", "<=", ">=", "==", "&&", "||", "!", "&", "|"]


def get_file_content():
    # Gets content from the input file (input.in)
    file = open("input.in", "r")
    content = file.read()
    file.close()
    return content


def check_keyword(word):
    if word in keywords:
        return word


def scan_content(content):
    for char in content:
        pass
