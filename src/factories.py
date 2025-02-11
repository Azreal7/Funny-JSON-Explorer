from src.explorers import *

class AbstractExplorerFactory:
    def createPokerfaceExplorer(self):
        raise NotImplementedError
    
    def createConfigIconExplorer(self):
        raise NotImplementedError
    
class TreeExplorerFactory(AbstractExplorerFactory):
    def createPokerfaceExplorer(self):
        return TreePokerfaceExplorer()
    
    def createConfigIconExplorer(self):
        return TreeConfigIconExplorer()

class RectangleExplorerFactory(AbstractExplorerFactory):
    def createPokerfaceExplorer(self):
        return RectanglePokerfaceExplorer()
    
    def createConfigIconExplorer(self):
        return RectangleConfigIconExplorer()