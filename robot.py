from weapons import Weapon
from dinosaur import Dinosaur


class Robot:
    #robot characteristics
    def __init__(self, name, health, weapon):
        self.name = name
        self.health = health
        self.attack_weapon = weapon
        pass


     #set been attack method causes health loss
    def robot_attack(self, dino_health):
        self.attack -= dino_health
        
robot_1 = ("r2d2", 10, [""])