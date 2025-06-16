from contextlib import nullcontext

from AMBTokensPKG import START_PROGRAM
from AMBTokensPKG.Assignment import Assignment
from AMBTokensPKG.END_PROGRAM import END_PROGRAM
from AMBTokensPKG.HardOpen import HardOpen
from AMBTokensPKG.MultOp import MultOp
from AMBTokensPKG.SoftOpen import SoftOpen


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
        elif(token == "END_PROGRAM"):
            tok = END_PROGRAM.END_PROGRAM()
        elif (token == "START_SUB"):
            tok = START_SUB.START_SUB()
        elif (token == "END_SUB"):
            tok = END_SUB.END_SUB()
        elif (token == "GOSUB"):
            tok = GOSUB.GOSUB()
        elif (token == "CODE"):
            tok = CODE.CODE()
        elif (token == "IF"):
            tok = IF.IF()
        elif (token == "THEN"):
            tok = THEN.THEN()
        elif (token == "ELSE"):
            tok = ELSE.ELSE()
        elif (token == "END_IF"):
            tok = END_IF.END_IF()
        elif (token == "WHILE"):
            tok = WHILE.WHILE()
        elif (token == "DO"):
            tok = DO.DO()
        elif (token == "END_WHILE"):
            tok = END_WHILE.END_WHILE()
        elif (token == "INT"):
            tok = INT.INT()
        elif (token == "STRING"):
            tok = STRING.STRING()
        elif (token == "PRINT"):
            tok = PRINT.PRINT()
        elif (token == "INPUT_INT"):
            tok = INPUT_INT.INPUT_INT()
        elif (token == "INPUT_STRING"):
            tok = INPUT_STRING.INPUT_STRING()
        elif (token == "("):
            tok = SoftOpen.SoftOpen()
        elif (token == ")"):
            tok = SoftClose.SoftClose()
        elif (token == "["):
            tok = HardOpen.HardOpen()
        elif (token == "]"):
            tok = HardClose.HardClose()
        elif (token == ";"):
            tok = Semi.Semi()
        elif (token == ":="):
            tok = Assignment.Assignment()
        elif (token == ":"):
            tok = Colon.Colon()
        elif (token == "*"):
            tok = MultOp.MultOp(MultOp.Operand.MULT)
        elif (token == "/"):
            tok = MultOp.MultOp(MultOp.Operand.DIVIDE)
        elif (token == "+"):
            tok = AddOp.AddOp(AddOp.Operand.ADD)
        elif (token == "-"):
            tok = AddOp.AddOp(AddOp.Operand.MINUS)
        elif (token == "<"):
            tok = CompOp.CompOp(CompOp.Operand.LESS_THAN)
        elif (token == ">"):
            tok = CompOp.CompOp(CompOp.Operand.GREATER_THAN)
        elif (token == "=<"):
            tok = CompOp.CompOp(CompOp.Operand.LESS_THAN_OR_EQUAL)
        elif (token == "=>"):
            tok = CompOp.CompOp(CompOp.Operand.GREATER_THAN_OR_EQUAL)
        elif (token == "="):
            tok = CompOp.CompOp(CompOp.Operand.EQUAL)
        elif (token == "!="):
            tok = CompOp.CompOp(CompOp.Operand.NOT_EQUAL)
        else:
            ## Begin DFA Implementation of the SYMBOL COLLECTIONS
            ## go character by character in token (the current string token)
            ## determine its going to be a:
            ## number
            ## characterString
            ## label
            ## or failure (32ab, 3*2 would also fail since not proper spacing)
            ## a failure would set tok to be None
            for char in token:
                if (char.isdigit()):
                    if (int(char) == 0):
                        print('hi')
                elif (char == '-'):
                    print('start of negative')


        if (tok == None):
            raise SystemError('Tokenizing error. Bad token' + token)
        tokens.append(tok)
    return tokens