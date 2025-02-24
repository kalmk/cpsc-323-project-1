from checker import *

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


symbols = {
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
    regex = []

   
    for line_number, line in enumerate(lines, start=1):
        print()
        print(f"Line to scan: #{line_number}")
        print(f"{line}")
        for char in line:
            dummy.append(char)

            print(f"Dummy current: {dummy}")

            if char == " ":
                # print("in empty")
                test_for_identifier = ''.join(dummy)
                print(f"test: {test_for_identifier}")
                if identifier_checker(test_for_identifier):
                    regex.append(test_for_identifier)
                    print(f"regex appended. {regex}")
                dummy.pop()
            elif char in symbols:
                print(symbols[char])
                dummy.clear()
            elif char == '\n':
                print("newlines")
                dummy.clear()
            else:
                word = ''.join(dummy)
                if word in keywords:
                    print(keywords[word])
                    dummy.clear()

