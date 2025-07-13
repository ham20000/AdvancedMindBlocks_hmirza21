#parameter takes in list of AMBTokens
from AMBNodes import AMBNodes
from AMBPTNodes import Program
from AMBTokensPKG.AMBTokens import AMBTokens

class AMBParseTreeGenerator:
    currentToken: int = 0
    code: list[AMBTokens]
    root: AMBNodes = None

    def generateParseTree(code: list[AMBTokens]):
        AMBParseTreeGenerator.code = code
        AMBParseTreeGenerator.currentToken = 0
        AMBParseTreeGenerator.root = Program.program()

