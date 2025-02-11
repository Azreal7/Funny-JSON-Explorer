import sys
from src.factories import *
from src.explorers import *
from src.builder import JSONBuilder

if __name__ == "__main__":
    if len(sys.argv) != 7 or sys.argv[1] != "-f" or sys.argv[3] != "-s" or sys.argv[5] != "-i":
        print("Usage: python JSONExplorer.py -f <json_file> -s <style> -i <icon_family>")
        sys.exit(1)

    json_file = sys.argv[2]
    style = sys.argv[4]
    iconFamily = sys.argv[6]

    factory = AbstractExplorerFactory()
    explorer = None

    if style == "tree":
        factory = TreeExplorerFactory()
    elif style == "rectangle":
        factory = RectangleExplorerFactory()
    else:
        raise ValueError("Unknown style")

    if iconFamily == "poker":
        explorer = factory.createPokerfaceExplorer()
    elif iconFamily == "config":
        explorer = factory.createConfigIconExplorer()
    else:
        raise ValueError("Unknown icon family")

    builder = JSONBuilder()
    root = builder.build(json_file)
    explorer.view(root)