from AMBTokensPKG import Symbols
from enum import Enum

class CompOp(Symbols.Symbols):
    def __init__(self, op):
        self.op = op ## potential to equal any Operand value, check enum below

## Enum used for determining what type of compOp this token is
class Operand(Enum):
    LESS_THAN = '<'
    GREATER_THAN = '>'
    LESS_THAN_OR_EQUAL = '=<'
    GREATER_THAN_OR_EQUAL = '=>'
    EQUAL = '='
    NOT_EQUAL = '!='