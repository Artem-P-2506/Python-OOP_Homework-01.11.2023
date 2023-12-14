from Materials.Material import *

class Wood(Material):
    def __init__(self, materialType = "WOOD", color = "BROWN", weight = 250):
        super().__init__(materialType, color, weight)