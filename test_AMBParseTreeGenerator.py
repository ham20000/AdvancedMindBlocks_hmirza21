from AMBParseTreeGenerator import AMBParseTreeGenerator
from AMBTokensPKG.START_PROGRAM import START_PROGRAM


def test_generate_parse_tree():
    code = [START_PROGRAM(children=[])]
    AMBParseTreeGenerator.generateParseTree(code)