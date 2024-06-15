class Component:
    def display(self):
        raise NotImplementedError

class Composite(Component):
    def __init__(self, name, style, icon_factory, depth):
        self.style = style
        self.name = name
        self.children = []
        self.iconFactory = icon_factory
        self.depth = depth

    def add(self, component):
        self.children.append(component)

    def remove(self, component):
        self.children.remove(component)

    def get_children(self):
        return self.children

    def display(self, display_buffer=[]):
        if self.style == "tree":
            if self.depth == 1:
                display_buffer.append("├─" + self.iconFactory.get_icon("node") + self.name)
            elif self.depth > 1:
                display_buffer.append("|" + " " * (2 * (self.depth - 1) - 1) + "└─" + self.iconFactory.get_icon("node") + self.name)
        
        elif self.style == "rectangle":
            if self.depth == 1:
                display_buffer.append("├─" + self.iconFactory.get_icon("node") + self.name)
            elif self.depth > 1:
                line = "|"
                for _ in range(1, self.depth - 2, 2):
                    line += " " * 2 + "|"
                line += " " * 2 + "├─"
                line += self.iconFactory.get_icon("node") + self.name
                display_buffer.append(line)


class Leaf(Component):
    def __init__(self, name, style, icon_factory, depth):
        self.style = style
        self.name = name
        self.iconFactory = icon_factory
        self.depth = depth

    def display(self, display_buffer=[]):
        if self.style == "tree":
            if self.depth == 1:
                display_buffer.append("├─" + self.iconFactory.get_icon("leaf") + self.name)
            elif self.depth > 1:
                display_buffer.append("|" + " " * (2 * (self.depth - 1) - 1) + "└─" + self.iconFactory.get_icon("leaf") + self.name)

        elif self.style == "rectangle":
            if self.depth == 1:
                display_buffer.append("├─" + self.iconFactory.get_icon("node") + self.name)
            elif self.depth > 1:
                line = "|"
                for _ in range(1, self.depth - 1, 2):
                    line += " " * 2 + "|"
                line += " " * 2 + "├─"
                line += self.iconFactory.get_icon("node") + self.name
                display_buffer.append(line)


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
            if isinstance(node, Composite):
                for child in reversed(node.get_children()):
                    self.stack.append(child)
            return node
        else:
            return None