class Component:
    def display(self):
        raise NotImplementedError

class Composite(Component):
    def __init__(self, name, depth):
        self.name = name
        self.children = []
        self.depth = depth
        self.type = "node"

    def addChild(self, component):
        self.children.append(component)

    def removeChild(self, component):
        self.children.remove(component)

    def getChildren(self):
        return self.children
    

class TreeIterator:
    def getNext(self):
        raise NotImplementedError
    def hasMore(self):
        raise NotImplementedError
    
class DFSIterator(TreeIterator):
    def __init__(self, root):
        self.element = root
        self.stack = [root]
    
    def hasMore(self):
        return len(self.stack) > 0

    def getNext(self):
        if self.hasMore():
            node = self.stack.pop()
            if node.getChildren() == []:
                node.type = "leaf"
            for child in reversed(node.getChildren()):
                self.stack.append(child)
            return node
        else:
            return None