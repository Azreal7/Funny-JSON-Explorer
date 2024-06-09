class Component:
    def display(self, depth=0, display_buffer=[]):
        raise NotImplementedError

class Composite(Component):
    def __init__(self, name, style):
        self.style = style
        self.name = name
        self.children = []

    def add(self, component):
        self.children.append(component)

    def remove(self, component):
        self.children.remove(component)

    def get_children(self):
        return self.children

    def display(self, iconFactory, depth=0, display_buffer=[]):
        if self.style == "tree":
            if depth == 1:
                display_buffer.append("├─" + iconFactory.get_icon("node") + self.name)
            elif depth > 1:
                display_buffer.append("|" + " " * (2 * (depth - 1) - 1) + "└─" + iconFactory.get_icon("node") + self.name)
            for child in self.children:
                child.display(iconFactory, depth + 1, display_buffer)
        
        elif self.style == "rectangle":
            if depth == 1:
                display_buffer.append("├─" + iconFactory.get_icon("node") + self.name)
            elif depth > 1:
                line = "|"
                for i in range(1, depth - 2, 2):
                    line += " " * 2 + "|"
                line += " " * 2 + "├─"
                line += iconFactory.get_icon("node") + self.name
                display_buffer.append(line)
            for child in self.children:
                child.display(iconFactory, depth + 1, display_buffer)


class Leaf(Component):
    def __init__(self, name, style):
        self.style = style
        self.name = name

    def display(self, iconFactory, depth=0, display_buffer=[]):
        if self.style == "tree":
            display_buffer.append("|" + " " * (2 * (depth - 1) - 1) + "└─" + iconFactory.get_icon("leaf") + self.name)

        elif self.style == "rectangle":
            if depth == 1:
                display_buffer.append("├─" + iconFactory.get_icon("node") + self.name)
            elif depth > 1:
                line = "|"
                for i in range(1, depth - 1, 2):
                    line += " " * 2 + "|"
                line += " " * 2 + "├─"
                line += iconFactory.get_icon("node") + self.name
                display_buffer.append(line)
