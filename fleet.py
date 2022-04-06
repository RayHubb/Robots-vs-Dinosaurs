from robot import Robot


class Fleet(Robot):
    def __init__(self, robot_fleet):
        self.robot_fleet = robot_fleet

    def create_fleet(self):
        self.robot_fleet = []
        robot1 = Robot("Jax", 40, 300)
        robot2 = Robot("Oscar", 50, 250)
        robot3 = Robot("Dexter", 45, 275)
        self.robot_fleet.append(robot1)
        self.robot_fleet.append(robot2)
        self.robot_fleet.append(robot3)
        for bot in self.robot_fleet:
            print(bot)
        print(self.robot_fleet)
        return self.robot_fleet
        