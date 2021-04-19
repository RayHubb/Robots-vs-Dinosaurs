from weapons import Weapon
from dinosaur import Dinosaur


class Robot:
    def __init__(self, name, health, power_level, robotweapon):
        self.name = name
        self.health = health
        self.power_level = power_level
        self.weapon = robotweapon

    def attack(self, name):
        if self.health > 0:
            print(self.name + ' is attacking!')
            import dinosaur
            dinosaur.health -= 35
            print(dinosaur.name + " has" + dinosaur.health + " left!")


