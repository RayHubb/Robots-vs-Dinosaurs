import robots


class Fleet:
    def __init__(self):
        self.robot_team = []

    def create_fleet(self):
        robot1 = robots.Robot('R2D2', 250, 100)
        robot2 = robots.Robot('C3PO', 175, 70)
        robot3 = robots.Robot('R4', 150, 60)
        self.robot_team.append(robot1, robot2, robot3)
        print(self.robot_team)


Fleet.create_fleet()