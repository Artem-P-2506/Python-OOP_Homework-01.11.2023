class Material:
    def __init__(self, materialType, color, weight):
        self.materialType = materialType
        self.color = color
        self.weight = weight

    def __str__(self):
        return f"\nMarerial:\t{str(self.materialType)}\nColor:\t{str(self.color)}\nWeight:\t{str(self.weight)}"