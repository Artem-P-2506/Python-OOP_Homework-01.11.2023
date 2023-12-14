import json
from Materials.Leather import *
from Materials.Metal import *
from Materials.Plastic import *
from Materials.Stone import *
from Materials.Thread import *
from Materials.Wood import *

# Инициализирую кортеж вместо массива:
MATERIALS = (Leather(), Metal(), Plastic(), Stone(), Thread(), Wood())

if __name__ == "__main__":
    # Сериализация массива материалов:
    materialsDICT = []
    for item in MATERIALS:
        materialsDICT.append(item.__dict__)

    # Запись полученного массива в файл:
    with open("materials.json", "w") as file:
        materialsJSON = json.dumps(materialsDICT)
        file.write(materialsJSON)

    # Чтение и сохранение информации из файла:
    with open("materials.json", "r") as file:
        materialsKWARGS = json.load(file)

    # Десериализация массива материалов:
    newMaterials = []
    for item in materialsKWARGS:
        if item['materialType'] == 'LEATHER':
            newMaterials.append(Leather(**item))
        elif item['materialType'] == 'METAL':
            newMaterials.append(Metal(**item))
        elif item['materialType'] == 'PLASTIC':
            newMaterials.append(Plastic(**item))
        elif item['materialType'] == 'STONE':
            newMaterials.append(Stone(**item))
        elif item['materialType'] == 'THREAD':
            newMaterials.append(Thread(**item))
        elif item['materialType'] == 'WOOD':
            newMaterials.append(Wood(**item))
        else:
            print("ERROR - Invalid type of material!")

        # Вывод полученного массива десериализованных материалов:
        for item in newMaterials:
            print(item)