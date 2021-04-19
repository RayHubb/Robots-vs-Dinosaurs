from robot import Robot


class Dinosaur:
    def __init__(self, type, health, energy, attack_power):
        self.type = type
        self.health = health
        self.energy = energy
        self.attack_power = attack_power

    def attack(self):
        if self.health > 0:
            print(self.name + ' is attacking!')
            Dinosaur.health -= 35
            print(Dinosaur.name + " has" + Dinosaur.health + " left!")
