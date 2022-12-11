from weapons import Weapon
from dinosaur import Dinosaur


class Robot:
    #robot characteristics
    def __init__(self):
        self.name = "r2d2"
        self.health = 20
        self.attack_weapon = []
        pass


     #set been attack method causes health loss
    def robot_attack(self, dino_health):
        self.attack -= dino_health
        
