class Robot:
    def __init__(self):
        self.name = ''
        self.health = ''
        self.power_level = ''
        self.weapon = ''
        self.attack_power = ''

    def fill_data(self):
        self.name = input("Name the Robot!")
        self.health = int(input('Enter the health level from 50 - 200'))
        self.power_level = int(input('Enter the robots power level from 5 - 10'))
        self.weapon = input('Choose the weapon')
        self.attack_power = int(input('Enter the attack power from 20 - 75'))

    def print_data(self):
        print('Name        :', self.name)
        print('Health      :', self.health)
        print('Power Level :', self.power_level)
        print('Weapon      :', self.weapon)
        print('Attack Power:', self.attack_power)


#this is the logic I will use in the fleet and herd classes later on
#robot_team = []
#for i in range(3):
#    robot = Robot()
#   robot.fill_data()
#    robot_team.append(robot)
#print(robot_team)

#for i in range(3):
#    robot_team[i].print_data()
#    print('-------------------')
#print(robot_team)

