from contextlib import nullcontext
import shlex
import AMBTokensPKG
from AMBTokensPKG import *

def tokenize(fileName):
    tokens = []
    #Read file
    #Turn file into giant String
    exampleData = "( 4 * 2 )"

    #Turn string into array of strings split on spaces
    exampleDataTokens = exampleData.split()

    dataTokens = shlex.split(fileName, posix=False)

    for token in dataTokens:
        tok = None

        # Will check token string and change tok to its corresponding token class
        if(token == "START_PROGRAM"):
            tok = AMBTokensPKG.START_PROGRAM.START_PROGRAM(children= [])
        elif(token == "END_PROGRAM"):
            tok = AMBTokensPKG.END_PROGRAM.END_PROGRAM(children= [])
        elif (token == "START_SUB"):
            tok = AMBTokensPKG.START_SUB.START_SUB(children= [])
        elif (token == "END_SUB"):
            tok = AMBTokensPKG.END_SUB.END_SUB(children= [])
        elif (token == "GOSUB"):
            tok = AMBTokensPKG.GOSUB.GOSUB(children= [])
        elif (token == "CODE"):
            tok = AMBTokensPKG.CODE.CODE(children= [])
        elif (token == "IF"):
            tok = AMBTokensPKG.IF.IF(children= [])
        elif (token == "THEN"):
            tok = AMBTokensPKG.THEN.THEN(children= [])
        elif (token == "ELSE"):
            tok = AMBTokensPKG.ELSE.ELSE(children= [])
        elif (token == "END_IF"):
            tok = AMBTokensPKG.END_IF.END_IF(children= [])
        elif (token == "WHILE"):
            tok = AMBTokensPKG.WHILE.WHILE(children= [])
        elif (token == "DO"):
            tok = AMBTokensPKG.DO.DO(children= [])
        elif (token == "END_WHILE"):
            tok = AMBTokensPKG.END_WHILE.END_WHILE(children= [])
        elif (token == "INT"):
            tok = AMBTokensPKG.INT.INT(children= [])
        elif (token == "STRING"):
            tok = AMBTokensPKG.STRING.STRING(children= [])
        elif (token == "PRINT"):
            tok = AMBTokensPKG.PRINT.PRINT(children= [])
        elif (token == "INPUT_INT"):
            tok = AMBTokensPKG.INPUT_INT.INPUT_INT(children= [])
        elif (token == "INPUT_STRING"):
            tok = AMBTokensPKG.INPUT_STRING.INPUT_STRING(children= [])
        elif (token == "("):
            tok = AMBTokensPKG.SoftOpen.SoftOpen(children= [])
        elif (token == ")"):
            tok = AMBTokensPKG.SoftClose.SoftClose(children= [])
        elif (token == "["):
            tok = AMBTokensPKG.HardOpen.HardOpen(children= [])
        elif (token == "]"):
            tok = AMBTokensPKG.HardClose.HardClose(children= [])
        elif (token == ";"):
            tok = AMBTokensPKG.Semi.Semi(children= [])
        elif (token == ":="):
            tok = AMBTokensPKG.Assignment.Assignment(children= [])
        elif (token == ":"):
            tok = AMBTokensPKG.Colon.Colon(children= [])
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
            ## determine it's going to be a:
            ## number
            ## characterString
            ## label
            ## or failure (32ab, 3*2 would also fail since not proper spacing)
            ## a failure would set tok to be None

            ## checking if token is number

            if(isTokenNumber(token)):
                tok = AMBTokensPKG.Number.Number(children= [])

            ## checking if token is a CharacterString

            if(isTokenCharacterString(token)):
                tok = AMBTokensPKG.CharacterString.CharacterString(children= [])

            ## checking if token is Label

            if(isTokenLabel(token)):
                tok = AMBTokensPKG.Label.Label(children= [])


        if (tok == None):
            raise SystemError('Tokenizing error. Bad token: ' + token)
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

# checks if token is a label for a variable
# must start with alpha, rest of label may only be either digits or alphas
def isTokenLabel(token):
    detectError = False

    if(not token[0].isalpha()):
        detectError = True

    for index, char in enumerate(token):
        if(not char.isdigit() and not char.isalpha()):
            detectError = True

    return not detectError

