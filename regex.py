def identifer_regex(string):
    # Check if first char is ([a - Z])
    if not (string[0].isalpha()):
        return False

    # Check if the rest of the string is ([a - Z] | [0 - 9])*
    for char in string[1:]:
        if not (char.isalpha() or char.isdigit()):
            return False

    return True


def number_regex(string):
    # Check if first char is ([0 - 9])
    if not (string[0].isdigit()):
        return False

     # Check if the rest of string is ([0 - 9])*
    for char in string[1:]:
        if not (string[0].isdigit()):
            return False

    return True


def comment_regex(string):
    pass
