from robots import Robot


class Dinosaur:
    def __init__(self, type, health, energy, attack_power):
        self.type = type
        self.health = health
        self.energy = energy
        self.attack_power = attack_power


    def fill_data(self):
        self.type = input("What type of Dinosaur?")
        self.health = int(input('Enter the health level from 50 - 200'))
        self.energy = int(input('Enter the power level from 5 - 10'))
        self.attack_power = int(input(''))

    def print_data(self):
        print('Type        :', self.type)
        print('Health      :', self.health)
        print('Energy      :', self.energy)
        print('Attack Power:', self.attack_power)

    def dino_attack(self, robot):
        if self.health > 1:
            Robot.health
        else:
            print(self.dinosaur.type)


