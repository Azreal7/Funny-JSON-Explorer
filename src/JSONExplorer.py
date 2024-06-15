from src.factories import TreeStyleFactory, RectangleStyleFactory, PokerFaceIconFactory, NothingIconFactory, configIconFactory
from src.builder import JSONBuilder
from src.viewer import Viewer

class JSONExplorer:
    def __init__(self, style_factory, icon_factory):
        self.style_factory = style_factory
        self.icon_factory = icon_factory
        self.display_buffer = []

    def run(self, json_file):
        builder = JSONBuilder(self.style_factory, self.icon_factory)
        root = builder.build(json_file)
        viewer = Viewer(root)
        viewer.display()
