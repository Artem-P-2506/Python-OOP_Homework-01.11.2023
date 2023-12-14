from Materials.Material import *

class Thread(Material):
    def __init__(self, materialType = "THREAD", color = "WHITE", weight = 100):
        super().__init__(materialType, color, weight)