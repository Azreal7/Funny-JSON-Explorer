import sys
from src.factories import TreeStyleFactory, RectangleStyleFactory, PokerFaceIconFactory, NothingIconFactory, configIconFactory
from src.JSONExplorer import JSONExplorer

if __name__ == "__main__":
    if len(sys.argv) != 7 or sys.argv[1] != "-f" or sys.argv[3] != "-s" or sys.argv[5] != "-i":
        print("Usage: python JSONExplorer.py -f <json_file> -s <style> -i <icon_family>")
        sys.exit(1)

    json_file = sys.argv[2]
    style = sys.argv[4]
    icon_family = sys.argv[6]

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
    elif icon_family == "config":
        icon_factory = configIconFactory()
    else:
        raise ValueError("Unknown icon family")

    explorer = JSONExplorer(style_factory, icon_factory)
    explorer.run(json_file)