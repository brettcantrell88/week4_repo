# As a developer, I want a Robot to 
# have the ability to attack a Dinosaur 
# on a Battlefield. 
# This attack method should lower 
# the Dinosaur’s health by the 
# attack_power of the Robot’s 
# active_weapon

from dinosaur import Dinosaur
from robot import Robot

class Battlefield:
    def __init__(self):
        self.dinosaur = Dinosaur()       
        self.robot = Robot()
        self.dinosaur.attack(self.robot)
            