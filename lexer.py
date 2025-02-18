

def get_source_code():
    # Gets source code from input.in and removes all whitespaces
    # and combines all words into one single string to start lexing.
    file = open("input.in", "r")

    dummy = file.read()
    source_code = dummy.split()

    words = []
    for word in source_code:
        words.append(word)

    result = "".join(words)

    return result


def identify_lexemes(source_code):
    lexemes = []

    for char in source_code:
        pass
