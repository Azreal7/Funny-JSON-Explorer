from components import Composite, Leaf

class StyleFactory:
    def create_component(self, name, is_leaf):
        raise NotImplementedError

class TreeStyleFactory(StyleFactory):
    def create_component(self, name, is_leaf):
        if is_leaf:
            return Leaf(name, "tree")
        else:
            return Composite(name, "tree")

class RectangleStyleFactory(StyleFactory):
    def create_component(self, name, is_leaf):
        if is_leaf:
            return Leaf(name, "rectangle")
        else:
            return Composite(name, "rectangle")

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