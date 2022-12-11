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
        self.dinosaur.attack(self.obot)
        self.robot.attack(self.dinosaur)
        
    def __init__(self):
        pass

    def start_game(self):
        print("Let the games begin. May the odds be ever in your favor.")

    def display_welcome(self):
        print("Welcome to the show! Today we have a fan favorite, {self.dinosaur.name}, and his opponent {self.robot.name}, who's storied past show him to be a top contender. Who will take home the crown? ")

    def run_battle(self):
        print("Round 1")
        print("The battle has begun! {self.dinosaur.name} just attacked {self.robot.name}!")
        Dinosaur.dino_attack -= Robot.health
        print("{self.robot.name} now has {self.robot.health} remaining.")
        print("{self.dinosaur.name} has attacked {self.robot.name}.")
        Robot.robot_attack -= Dinosaur.health
        print("{self.dinosaur.name} now has {self.dinosaur.health} remaining.")
