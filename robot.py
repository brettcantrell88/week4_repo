from weapons import Weapon

#robot characteristics
class Robot:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.attack_weapon = Weapon("gun", 25)
        pass

    #set been attack method causes health loss
    def attack(self, dinosaur):
        dinosaur.health -= self.attack_weapon.attack
        print(f"{self.name} has attacked {dinosaur.name} for {self.attack_weapon.attack} damage leaving {dinosaur.name} with {dinosaur.health} remaining.")

