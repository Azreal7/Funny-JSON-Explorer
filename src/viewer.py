from src.components import Component, Leaf, Composite, TreeIterator, DFSIterator
class Viewer:
    def __init__(self, component):
        self.component = component
        self.iterator = None

    def display(self):
        display_buffer = []
        # self.component.display(display_buffer) # 需要改为迭代器模式

        self.iterator = DFSIterator(self.component)
        while self.iterator.hasMore():
            node = self.iterator.getNext()
            node.display(display_buffer)

        max_length = 0
        for line in display_buffer:
            max_length = max(max_length, len(line))

        if self.component.style == "tree":
            n = len(display_buffer)
            for i in range(n - 1, 0, -1):
                if display_buffer[i].startswith("|"):
                    display_buffer[i] = " " + display_buffer[i][1:]
                elif display_buffer[i].startswith("├"):
                    display_buffer[i] = "└" + display_buffer[i][1:]
                    break

        elif self.component.style == "rectangle":
            n = len(display_buffer)
            display_buffer[0] = "┌" + display_buffer[0][1:]
            for i in range(0, n):
                display_buffer[i] += (max_length + 3 - len(display_buffer[i])) * "─" + "│"
            display_buffer[0] = display_buffer[0][:-1] + "┐"
            display_buffer[n - 1] = display_buffer[n - 1][:-1] + "┘"
            display_buffer[n - 1] = "└" + display_buffer[n - 1][1:]
            display_buffer[n - 1] = display_buffer[n - 1].replace("├", "┴")
            for i in range(1, n - 1):
                display_buffer[i] = display_buffer[i][:-1] + "┤"
            for i in range(1, len(display_buffer[n - 1])):
                if display_buffer[n - 1][i:2] == " ":
                    display_buffer[n - 1] = display_buffer[n - 1][0:3].replace(" ", "─") + display_buffer[n - 1][3:]
                else:
                    break

        for line in display_buffer:
            print(line)

