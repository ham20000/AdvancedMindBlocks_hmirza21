import AMBNodes

class AMBNodes():
    def __init__(self,children: list[AMBNodes]):
        self.children = children

    def addChild(self, node: AMBNodes):
        self.children.append(node)

    def getChildren(self) -> list[AMBNodes]:
        return self.children