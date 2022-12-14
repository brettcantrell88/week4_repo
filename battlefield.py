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
        self.dinosaur = Dinosaur("Little Foot", 100, 15)       
        self.robot = Robot("r2d2", 100)
     

    def start_game(self):
        print("Let the games begin. May the odds be ever in your favor.")
        self.display_welcome()
        self.run_battle()

    def display_welcome(self):
        print(f"Welcome to the show! Today we have a fan favorite, {self.dinosaur.name}, and his opponent {self.robot.name}, who's storied past show him to be a top contender. Who will take home the crown? ")

    def run_battle(self):
        while self.robot.health > 0 and self.dinosaur.health > 0:
            self.robot.attack(self.dinosaur)
            self.dinosaur.attack(self.robot)
        if self.robot.health < self.dinosaur.health:
            print(f"{self.dinosaur.name} is the victor")
        elif self.robot.health > self.dinosaur.health:
            print(f"{self.robot.name} is the victor!")
        
