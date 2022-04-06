from weapon import Weapon


class Robot(Weapon):
    def __init__(self, name, power_level, health):
        self.name = name
        self.power_level = power_level
        self.health = health
        self.weapon = Weapon("Sword", 25)

    def robot_attack(self):
        if self.health > 0:
            return print(self.name + " is attacking with its " + self.weapon + "!")
