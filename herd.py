from dinosaur import Dinosaur


class Herd(Dinosaur):
    def __init__(self, dinosaur_herd):
        self.dinosaur_herd = dinosaur_herd

    def create_herd(self):
        self.dinosaur_herd = []
        dino1 = Dinosaur("Rex", "T-Rex", 120, 75, 300)
        dino2 = Dinosaur("Tony", "Triceratops", 75, 50, 275)
        dino3 = Dinosaur("Ed", "Raptor", 100, 100, 200)
        self.dinosaur_herd.append(dino1)
        self.dinosaur_herd.append(dino2)
        self.dinosaur_herd.append(dino3)
        for dino in self.dinosaur_herd:
            print(dino.name + " the " + dino.dinosaur_type)
        print(self.dinosaur_herd)
        return self.dinosaur_herd

