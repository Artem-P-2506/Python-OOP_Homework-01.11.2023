from Materials.Material import *

class Metal(Material):
    def __init__(self, materialType = "METAL", color = "SILVER", weight = 500):
        super().__init__(materialType, color, weight)