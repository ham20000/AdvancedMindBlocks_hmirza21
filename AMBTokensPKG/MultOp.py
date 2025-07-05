from AMBTokensPKG import Symbols
from enum import Enum

class MultOp(Symbols.Symbols):
    def __init__(self, op):
        self.op = op ## equals either MULT or DIVIDE

## Enum used for determining what type of multOp this token is
class Operand(Enum):
    MULT = '*'
    DIVIDE = '/'