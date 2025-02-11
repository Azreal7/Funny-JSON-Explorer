import json
from src.components import Composite, DFSIterator, TreeIterator

class AbstractExplorer:
    def initBuffer(self):
        raise NotImplementedError
    
class AbstractTreeExplorer(AbstractExplorer):
    def initBuffer(self):
        raise NotImplementedError
    
    def view(self, root):
        displayBuffer = self.initBuffer(root)
        n = len(displayBuffer)
        for i in range(n - 1, 0, -1):
            if displayBuffer[i].startswith("|"):
                displayBuffer[i] = " " + displayBuffer[i][1:]
            elif displayBuffer[i].startswith("├"):
                displayBuffer[i] = "└" + displayBuffer[i][1:]
                break
        for line in displayBuffer:
            print(line)


class AbstractRectangleExplorer(AbstractExplorer):
    def initBuffer(self):
        raise NotImplementedError
    
    def view(self, root):
        displayBuffer = self.initBuffer(root)
        max_length = 0
        for line in displayBuffer:
            max_length = max(max_length, len(line))
        n = len(displayBuffer)
        displayBuffer[0] = "┌" + displayBuffer[0][1:]
        for i in range(0, n):
            displayBuffer[i] += (max_length + 3 - len(displayBuffer[i])) * "─" + "│"
        displayBuffer[0] = displayBuffer[0][:-1] + "┐"
        displayBuffer[n - 1] = displayBuffer[n - 1][:-1] + "┘"
        displayBuffer[n - 1] = "└" + displayBuffer[n - 1][1:]
        displayBuffer[n - 1] = displayBuffer[n - 1].replace("├", "┴")
        for i in range(1, n - 1):
            displayBuffer[i] = displayBuffer[i][:-1] + "┤"
        for i in range(1, len(displayBuffer[n - 1])):
            if displayBuffer[n - 1][i:2] == " ":
                displayBuffer[n - 1] = displayBuffer[n - 1][0:3].replace(" ", "─") + displayBuffer[n - 1][3:]
            else:
                break
        for line in displayBuffer:
            print(line)

    
class TreePokerfaceExplorer(AbstractTreeExplorer):
    def initBuffer(self, root):
        displayBuffer = []
        icons = {"leaf": "♤", "node": "♢"}
        iterator = DFSIterator(root)
        while iterator.hasMore():
            node = iterator.getNext()
            if node.depth == 1:
                displayBuffer.append("├─" + icons[node.type] + node.name)
            elif node.depth > 1:
                displayBuffer.append("|" + " " * (2 * (node.depth - 1) - 1) + "└─" + icons[node.type] + node.name)
        return displayBuffer


class TreeConfigIconExplorer(AbstractTreeExplorer):
    def getIcon(self):
        icons = {}
        with open("config/config.json") as f:
            data = json.load(f)
            for key, value in data.items():
                icons[key] = value
        return icons

    def initBuffer(self, root):
        displayBuffer = []
        icons = self.getIcon()
        iterator = DFSIterator(root)
        while iterator.hasMore():
            node = iterator.getNext()
            if node.depth == 1:
                displayBuffer.append("├─" + icons[node.type] + node.name)
            elif node.depth > 1:
                displayBuffer.append("|" + " " * (2 * (node.depth - 1) - 1) + "└─" + icons[node.type] + node.name)
        return displayBuffer


class RectanglePokerfaceExplorer(AbstractRectangleExplorer):
    def initBuffer(self, root):
        displayBuffer = []
        icons = {"leaf": "♤", "node": "♢"}
        iterator = DFSIterator(root)
        while iterator.hasMore():
            node = iterator.getNext()
            if node.depth == 1:
                displayBuffer.append("├─" + icons[node.type] + node.name)
            elif node.depth > 1:
                line = "|"
                for _ in range(1, node.depth - 1, 2):
                    line += " " * 2 + "|"
                line += " " * 2 + "├─"
                line += icons[node.type] + node.name
                displayBuffer.append(line)
        return displayBuffer

class RectangleConfigIconExplorer(AbstractRectangleExplorer):
    def getIcon(self):
        icons = {}
        with open("config/config.json") as f:
            data = json.load(f)
            for key, value in data.items():
                icons[key] = value
        return icons

    def initBuffer(self, root):
        displayBuffer = []
        icons = self.getIcon()
        iterator = DFSIterator(root)
        while iterator.hasMore():
            node = iterator.getNext()
            if node.depth == 1:
                displayBuffer.append("├─" + icons[node.type] + node.name)
            elif node.depth > 1:
                line = "|"
                for _ in range(1, node.depth - 1, 2):
                    line += " " * 2 + "|"
                line += " " * 2 + "├─"
                line += icons[node.type] + node.name
                displayBuffer.append(line)
        return displayBuffer