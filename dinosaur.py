class Dinosaur:
    def __init__(self, dino_type, health, energy, attack_power):
        self.type = dino_type
        self.health = health
        self.energy = energy
        self.attack_power = attack_power

    def attack(self, name):
        if self.health > 0:
            print(self.name + ' is attacking!')
            import robots
            robots.health -= 35
            print(robots.name + " has" + robots.health + " left!")
