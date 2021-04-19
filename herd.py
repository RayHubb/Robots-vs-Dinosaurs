import herd as herd

import dinosaur
from dinosaur import Dinosaur


class Herd:
    def __init__(self):
        self.dino_herd = []

    def create_herd(self):
        dino1 = dinosaur.Dinosaur('T-Rex', 300, 125, 75)
        dino2 = dinosaur.Dinosaur('Raptor', 200, 100, 70,)
        dino3 = dinosaur.Dinosaur('R4', 150, 125, 60)
        self.dino_herd.append(dino1, dino2, dino3)
        print(self.dino_herd)
