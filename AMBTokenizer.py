from contextlib import nullcontext

import AMBTokensPKG


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
            tok = AMBTokensPKG.START_PROGRAM.START_PROGRAM()
        elif(token == "END_PROGRAM"):
            tok = AMBTokensPKG.END_PROGRAM.END_PROGRAM()
        elif (token == "START_SUB"):
            tok = AMBTokensPKG.START_SUB.START_SUB()
        elif (token == "END_SUB"):
            tok = AMBTokensPKG.END_SUB.END_SUB()
        elif (token == "GOSUB"):
            tok = AMBTokensPKG.GOSUB.GOSUB()
        elif (token == "CODE"):
            tok = AMBTokensPKG.CODE.CODE()
        elif (token == "IF"):
            tok = AMBTokensPKG.IF.IF()
        elif (token == "THEN"):
            tok = AMBTokensPKG.THEN.THEN()
        elif (token == "ELSE"):
            tok = AMBTokensPKG.ELSE.ELSE()
        elif (token == "END_IF"):
            tok = AMBTokensPKG.END_IF.END_IF()
        elif (token == "WHILE"):
            tok = AMBTokensPKG.WHILE.WHILE()
        elif (token == "DO"):
            tok = AMBTokensPKG.DO.DO()
        elif (token == "END_WHILE"):
            tok = AMBTokensPKG.END_WHILE.END_WHILE()
        elif (token == "INT"):
            tok = AMBTokensPKG.INT.INT()
        elif (token == "STRING"):
            tok = AMBTokensPKG.STRING.STRING()
        elif (token == "PRINT"):
            tok = AMBTokensPKG.PRINT.PRINT()
        elif (token == "INPUT_INT"):
            tok = AMBTokensPKG.INPUT_INT.INPUT_INT()
        elif (token == "INPUT_STRING"):
            tok = AMBTokensPKG.INPUT_STRING.INPUT_STRING()
        elif (token == "("):
            tok = AMBTokensPKG.SoftOpen.SoftOpen()
        elif (token == ")"):
            tok = AMBTokensPKG.SoftClose.SoftClose()
        elif (token == "["):
            tok = AMBTokensPKG.HardOpen.HardOpen()
        elif (token == "]"):
            tok = AMBTokensPKG.HardClose.HardClose()
        elif (token == ";"):
            tok = AMBTokensPKG.Semi.Semi()
        elif (token == ":="):
            tok = AMBTokensPKG.Assignment.Assignment()
        elif (token == ":"):
            tok = AMBTokensPKG.Colon.Colon()
        elif (token == "*"):
            tok = AMBTokensPKG.MultOp.MultOp(AMBTokensPKG.MultOp.Operand.MULT)
        elif (token == "/"):
            tok = AMBTokensPKG.MultOp.MultOp(AMBTokensPKG.MultOp.Operand.DIVIDE)
        elif (token == "+"):
            tok = AMBTokensPKG.AddOp.AddOp(AMBTokensPKG.AddOp.Operand.ADD)
        elif (token == "-"):
            tok = AMBTokensPKG.AddOp.AddOp(AMBTokensPKG.AddOp.Operand.MINUS)
        elif (token == "<"):
            tok = AMBTokensPKG.CompOp.CompOp(AMBTokensPKG.CompOp.Operand.LESS_THAN)
        elif (token == ">"):
            tok = AMBTokensPKG.CompOp.CompOp(AMBTokensPKG.CompOp.Operand.GREATER_THAN)
        elif (token == "=<"):
            tok = AMBTokensPKG.CompOp.CompOp(AMBTokensPKG.CompOp.Operand.LESS_THAN_OR_EQUAL)
        elif (token == "=>"):
            tok = AMBTokensPKG.CompOp.CompOp(AMBTokensPKG.CompOp.Operand.GREATER_THAN_OR_EQUAL)
        elif (token == "="):
            tok = AMBTokensPKG.CompOp.CompOp(AMBTokensPKG.CompOp.Operand.EQUAL)
        elif (token == "!="):
            tok = AMBTokensPKG.CompOp.CompOp(AMBTokensPKG.CompOp.Operand.NOT_EQUAL)
        else:
            ## Begin DFA Implementation of the SYMBOL COLLECTIONS
            ## go character by character in token (the current string token)
            ## determine its going to be a:
            ## number
            ## characterString
            ## label
            ## or failure (32ab, 3*2 would also fail since not proper spacing)
            ## a failure would set tok to be None

            ## checking if token is number

            if(isTokenNumber(token)):
                tok = AMBTokensPKG.Number.Number()

            ## checking if token is a CharacterString




        if (tok == None):
            raise SystemError('Tokenizing error. Bad token' + token)
        tokens.append(tok)
    return tokens

# takes in string Token and checks if it is a number
def isTokenNumber(token):
    detectNonNum = False  ## turns to true if a non number is detected
    for index, char in enumerate(token):
        # check if this char is not a digit
        if (not char.isdigit()):
            # if char is not a digit, we need take into account that it might be a '-', denoting a negative number
            if (char == '-'):
                if(index > 0):
                    detectNonNum = True
            else:
                detectNonNum = True
    return not detectNonNum

# checks if token is a character string,
# must start with a quote and end with a quote, no quotes within quotes
def isTokenCharacterString(token):
    detectError = False # becomes true if char within token goes against the rules of a character string

    # needs to have 2 quotes, if string is 1 char long, then it cannot have 2 quotes
    if(len(token) < 2):
        detectError == True

    for index, char in enumerate(token):
        if(index == 0):
            if(not char == '"'):
                detectError = True
        elif(index == len(token) - 1):
            if(not char == '"'):
                detectError = True
        else:
            if(char == '"'):
                detectError = True

    return not detectError

