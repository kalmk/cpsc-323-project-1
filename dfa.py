states = ["q0", "q1", "q2", "q3", "q4", "q5", "q6", "q7", "q8", "q9", "q10", "q11", "q12", "q13", "q14", "q15", "q16", "q17", "q18", "q19", "q20", "q21", "q22", "q23", "q24", "q25", "q26", "q27", "q28", "q29", "q30", "q31"]

token_names = ["identifier", "number", "comment", "leftParen", "rightParen", "leftBracket", "rightBracket", "leftBrace", "rightBrace", "dot", "plus", "minus", "multiply", "divide", "modulus", "lessThan", "greaterThan", "assignment", "semicolon", "comma", "increment", "decrement", "lessThanEq", "greaterThanEq", "logicEqual", "logicANd", "logicOr", "logicNot", "bitAnd", "bitOr"]

token_keywords = ["int", "return", "if", "switch", "float", "while", "else", "case", "char", "for", "goto", "unsigned", "main", "break", "continue", "void"]

dfa_table = [
    #   a-Z   0     1-9   -     .     !     =     +     <     >     &     |     (     )     {     }     *     /     ;
    ["q1", "q5", "q3", "q4", None, "q9", "q29", "q11", "q14", "q16", "q18", "q20", "q22", "q23", "q24", "q25", "q26", "q27", "q31"],  # q0
    ["q2", "q2", "q2", None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],  # q1
    ["q2", "q2", "q2", None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],  # q2
    [None, "q3", "q3", None, "q7", None, None, None, None, None, None, None, None, None, None, None, None, None, None],  # q3
    [None, "q6", "q3", "q13", None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],  # q4
    [None, None, None, "q7", None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],  # q5
    [None, None, None, "q7", None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],  # q6
    ["q8", "q8", "q8", None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],  # q7
    ["q8", "q8", "q8", None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],  # q8
    [None, None, None, None, None, "q10", None, None, None, None, None, None, None, None, None, None, None, None, None],  # q9
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],  # q10
    [None, None, None, None, None, None, "q12", None, None, None, None, None, None, None, None, None, None, None, None],  # q11
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],  # q12
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],  # q13
    [None, None, None, None, None, None, "q15", None, None, None, None, None, None, None, None, None, None, None, None],  # q14
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],  # q15
    [None, None, None, None, None, None, "q17", None, None, None, None, None, None, None, None, None, None, None, None],  # q16
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],  # q17
    [None, None, None, None, None, None, None, None, None, None, "q19", None, None, None, None, None, None, None, None],  # q18
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],  # q19
    [None, None, None, None, None, None, None, "q21", None, None, None, None, None, None, None, None, None, None, None],  # q20
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],  # q21
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],  # q22
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],  # q23
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],  # q24
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],  # q25
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],  # q26
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, "q28", None],  # q27
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],  # q28
    [None, None, None, None, None, None, "q30", None, None, None, None, None, None, None, None, None, None, None, None],  # q29
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],  # q30
    ["q31", None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],  # q31
]

# need a current state and input variables to keep track