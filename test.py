# prototype

keywords = {
    'int': 'int',
    'float': 'float',
    'char': 'char',
    'main': 'main',
    'return': 'return',
    'while': 'while',
    'for': 'for',
    'break': 'break',
    'if': 'if',
    'else': 'else',
    'goto': 'goto',
    'continue': 'continue',
    'switch': 'switch',
    'case': 'case',
    'unsigned': 'unsigned',
    'void': 'void'
}


pair = {
    '(': 'leftParen',
    ')': 'rightParen',
    '[': 'leftBracket',
    ']': 'rightBracket',
    '{': 'leftBracket',
    '}': 'rightBracket',
    '.': 'dot',
    '+': 'plus',
    '-': 'minus',
    '*': 'multiply',
    '/': 'divide',
    '%': 'modulus',
    '<': 'lessThan',
    '>': 'greaterThan',
    '=': 'assignment',
    ';': 'semicolon',
    ',': 'comma',
    '++': 'increment',
    '--': 'decrement',
    '<=': 'lessThanEq',
    '>=': 'greaterThanEQ',
    '==': 'logicEqual',
    '&&': 'logicAnd',
    '||': 'logicOr',
    '!': 'logicNot',
    '&': 'bitAnd',
    '|': 'bitOr'
}


def scan_line():
    file = open("input.in", "r")
    lines = file.readlines()

    dummy = []

    # choose a specific line to scan for now
    for i in lines[2]:
        dummy.append(i)

        print(f"Dummy current: {dummy}")

        # check if number is before alphabet, and if so, then it is invalid, etc..

        if i == " ":
            dummy.pop()

        if i in pair:
            print(pair[i])
            dummy.clear()

        if i == '\n':
            print("newlines!")
            dummy.clear()

        if ''.join(dummy) in keywords:
            print(keywords[''.join(dummy)])
            dummy.clear()


