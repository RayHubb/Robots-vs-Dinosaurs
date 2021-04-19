import weapon
from dinosaur import Dinosaur
from weapon import Weapon




class Robot:
    def __init__(self, name, health, power_level)
        self.name = name
        self.health = health
        self.power_level = power_level
        self.weapon =


    def create_weapon(self):
        self.weapon = weapon.Weapon()


    def attack(self):
        if self.health > 0:
            print(self.name + ' is attacking!')
            Dinosaur.health -= 35
            print(Dinosaur.name + " has" + Dinosaur.health + " left!")


robot1 = Robot('R2D2', 250, 100, weapon.weapon1)
robot2 = Robot('C3PO', 175, 70, weapon.weapon2)
robot3 = Robot('R4', 150, 60, weapon.weapon3)