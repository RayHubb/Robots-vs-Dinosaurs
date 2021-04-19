from robots import Robot
from weapon import Weapon

class Fleet:
    def __init__(self):
        self.robot_team = []

    def create_fleet(self):
        robot1 = Robot('R2D2', 250, 100, sword)
        robot2 = Robot('C3PO', 175, 70, sword)
        robot3 = Robot('R4', 150, 60, sword)
        self.robot_team.append(robot1, robot2, robot3)
        print(self.robot_team)
