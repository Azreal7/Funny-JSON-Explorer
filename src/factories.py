from src.components import Composite, Leaf
import json

class StyleFactory:
    def create_component(self):
        raise NotImplementedError

class TreeStyleFactory(StyleFactory):
    def create_component(self, name, is_leaf, depth, icon_factory):
        if is_leaf:
            return Leaf(name, "tree", icon_factory, depth)
        else:
            return Composite(name, "tree", icon_factory, depth)

class RectangleStyleFactory(StyleFactory):
    def create_component(self, name, is_leaf, depth, icon_factory):
        if is_leaf:
            return Leaf(name, "rectangle", icon_factory, depth)
        else:
            return Composite(name, "rectangle", icon_factory, depth)

class IconFactory:
    def get_icon(self, node_type):
        raise NotImplementedError

class PokerFaceIconFactory(IconFactory):
    def get_icon(self, node_type):
        icons = {"node": "♢", "leaf": "♤"}
        return icons[node_type]

class NothingIconFactory(IconFactory):
    def get_icon(self, node_type):
        return " "

# config.json中，key为节点类型，value为节点图标
class configIconFactory(IconFactory):
    def get_icon(self, node_type):
        icons = {}
        with open("config\config.json") as f:
            data = json.load(f)
            for key, value in data.items():
                # print(key, value)
                icons[key] = value
        return icons[node_type]