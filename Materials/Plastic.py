from Materials.Material import *

class Plastic(Material):
    def __init__(self, materialType = "PLASTIC", color = "BLACK", weight = 150):
        super().__init__(materialType, color, weight)