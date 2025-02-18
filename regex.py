def identifer_regex(word):
    # Check if first char is ([a - Z])
    if not (word[0].isalpha()):
        return False

    # Check if the rest of the word is ([a - Z] | [0 - 9])*
    for char in word[1:]:
        if not (char.isalpha() or char.isdigit()):
            return False

    return True


def number_regex(word):
    # Check if first char is ([0 - 9])
    if not (word[0].isdigit()):
        return False

    # Check if the rest of word is ([0 - 9])*
    for char in word[1:]:
        if not (word[0].isdigit()):
            return False

    return True


def comment_regex(line):
        # Check if the first 2 chars of the line is //
        if not line.startswith("//"):
            return False

        # Check the end of the word for newline
        if not line.endswith("\n"):
            return False

        return True
