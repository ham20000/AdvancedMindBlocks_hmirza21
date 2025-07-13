import AMBParseTreeGenerator as PTG
from AMBPTNodes import AMBNodes
from AMBTokensPKG.AMBTokens import AMBTokens
from AMBTokensPKG.START_PROGRAM import START_PROGRAM


def program() -> AMBNodes:
    code = PTG.AMBParseTreeGenerator.code
    currentToken = PTG.AMBParseTreeGenerator.currentToken
    cur: AMBTokens = code[currentToken]
    print(type(cur).__name__)
    if(type(cur).__name__ == START_PROGRAM.__name__):
        node: AMBNodes = AMBNodes.AMBNodes(children = [])
        node.addChild(cur)
        PTG.AMBParseTreeGenerator.currentToken = PTG.AMBParseTreeGenerator.currentToken + 1
