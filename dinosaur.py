class Dinosaur:
    def __init__(self, name, dinosaur_type, energy, attack_power, health):
        self.name = name
        self.dinosaur_type = dinosaur_type
        self.energy = energy
        self.attack_power = attack_power
        self.health = health

    def dinosaur_attack(self):
        if self.health > 0:
            print(self.name + " is attacking!")

