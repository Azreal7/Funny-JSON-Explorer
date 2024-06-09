from factories import TreeStyleFactory, RectangleStyleFactory, PokerFaceIconFactory, NothingIconFactory
from builder import JSONBuilder

class JSONExplorer:
    def __init__(self, style_factory, icon_factory):
        self.style_factory = style_factory
        self.icon_factory = icon_factory
        self.display_buffer = []

    def run(self, json_file):
        builder = JSONBuilder(self.style_factory, self.icon_factory)
        root = builder.build(json_file)
        root.display(self.icon_factory, 0, self.display_buffer)

        if self.style_factory.__class__.__name__ == "TreeStyleFactory":
        # 对display_buffer进行处理
            n = len(self.display_buffer)
            for i in range(n - 1, 0, -1):
                if self.display_buffer[i].startswith("|"):
                    self.display_buffer[i] = " " + self.display_buffer[i][1:]
                elif self.display_buffer[i].startswith("├"):
                    self.display_buffer[i] = "└" + self.display_buffer[i][1:]
                    break
        
        if self.style_factory.__class__.__name__ == "RectangleStyleFactory":
            n = len(self.display_buffer)
            self.display_buffer[0] = "┌" + self.display_buffer[0][1:]
            for i in range(0, n):
                self.display_buffer[i] += (50 - len(self.display_buffer[i])) * "─" + "│"
            self.display_buffer[0] = self.display_buffer[0][:-1] + "┐"
            self.display_buffer[n - 1] = self.display_buffer[n - 1][:-1] + "┘"
            self.display_buffer[n - 1] = "└" + self.display_buffer[n - 1][1:]
            self.display_buffer[n - 1] = self.display_buffer[n - 1].replace("├", "┴")
            for i in range(1, n - 1):
                self.display_buffer[i] = self.display_buffer[i][:-1] + "┤"
            for i in range(1, len(self.display_buffer[n - 1])):
                if self.display_buffer[n - 1][i:2] == " ":
                    # 空格替换为"─"
                    self.display_buffer[n - 1] = self.display_buffer[n - 1][0:3].replace(" ", "─") + self.display_buffer[n - 1][3:]
                else:
                    break


        for line in self.display_buffer:
            print(line)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 4:
        print("Usage: python JSONExplorer.py <json_file> <style> <icon_family>")
        sys.exit(1)

    json_file = sys.argv[1]
    style = sys.argv[2]
    icon_family = sys.argv[3]

    if style == "tree":
        style_factory = TreeStyleFactory()
    elif style == "rectangle":
        style_factory = RectangleStyleFactory()
    else:
        raise ValueError("Unknown style")

    if icon_family == "poker":
        icon_factory = PokerFaceIconFactory()
    elif icon_family == "nothing":
        icon_factory = NothingIconFactory()
    else:
        raise ValueError("Unknown icon family")

    explorer = JSONExplorer(style_factory, icon_factory)
    explorer.run(json_file)
