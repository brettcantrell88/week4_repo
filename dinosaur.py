from weapons import Weapon
from robot import Robot


class Dinosaur:
#Dino class and characteristics
    def __init__ (self, dino_name, health, attack):
        self.name = dino_name
        self.health = health
        self.attack = attack
        pass

    #set attack methods causes health loss 
    def dino_attack(self, robot_health):
        self.attack -= robot_health
        
dino_1 = ("Litle Foot", 10, 2)

    

