from Materials.Material import *

class Leather(Material):
    def __init__(self, materialType = "LEATHER", color = "LIGHT BROWN", weight = 350):
        super().__init__(materialType, color, weight)