class Dinosaur:
    def __init__(self):
        self.type = ''
        self.health = ''
        self.energy = ''
        self.attack_power = ''

    def fill_data(self):
        self.type = input("What type of Dinosaur?")
        self.health = int(input('Enter the health level from 50 - 200'))
        self.energy = int(input('Enter the power level from 5 - 10'))
        self.attack_power = int(input('Enter the attack power from 20 - 75'))

    def print_data(self):
        print('Type        :', self.type)
        print('Health      :', self.health)
        print('Energy      :', self.energy)
        print('Attack Power:', self.attack_power)