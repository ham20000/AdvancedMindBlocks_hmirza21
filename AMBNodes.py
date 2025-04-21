class AMBNodes():
    def __init__(self,children):
        self.children = children

    def addChild(self, node):
        self.children.add(node)

    def getChildren(self):
        return self.children