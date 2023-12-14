from Materials.Material import *

class Stone(Material):
    def __init__(self, materialType = "STONE", color = "GRAY", weight = 350):
        super().__init__(materialType, color, weight)