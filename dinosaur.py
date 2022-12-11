from weapons import Weapon
from robot import Robot


class Dinosaur:
#Dino class and characteristics
    def __init__ (self):
        self.name = "Little Foot"
        self.health = 20
        self.attack = 2
        pass

    #set attack methods causes health loss 
    def dino_attack(self, robot_health):
        self.attack -= robot_health
        

    

