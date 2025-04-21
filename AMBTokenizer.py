from contextlib import nullcontext

import START_PROGRAM


def tokenize(fileName):
    tokens = []
    #Read file
    #Turn file into giant String
    exampleData = "( 4 * 2 )"

    #Turn string into array of strings split on spaces
    exampleDataTokens = exampleData.split()

    for token in exampleDataTokens:
        tok = None

        # Will check token string and change tok to its corresponding token class
        if(token == "START_PROGRAM"):
            tok = START_PROGRAM.START_PROGRAM()



    return tokens