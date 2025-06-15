import Symbols
from enum import Enum

class AddOp(Symbols.Symbols):
    def __init__(self, op):
        self.op = op ## equals either ADD or MINUS

## Enum used for determining what type of addOp this token is
class Operand(Enum):
    ADD = '+'
    MINUS = '-'