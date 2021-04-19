from dinosaur import Dinosaur
from weapon import Weapon


class Robot:
    def __init__(self, name, health, power_level, sword):
        self.name = name
        self.health = health
        self.power_level = power_level
        self.weapon = sword

    def choose_weapon(self):
        Weapon.assign_sword()

    def attack(self):
        if self.health > 0:
            print(self.name + ' is attacking!')
            Dinosaur.health -= 35
            print(Dinosaur.name + " has" + Dinosaur.health + " left!")
