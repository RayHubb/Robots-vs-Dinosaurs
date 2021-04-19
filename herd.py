import dinosaur
from dinosaur import Dinosaur


class Herd:
    def __init__(self):
        self.dino_herd = []

    for i in range(3):
        new_dino = Dinosaur()
        new_dino = dinosaur.fill_data()
        self.dino_herd.append(new_dino)

    for i in range(3):
        self.dino_herd[i].print_data()
