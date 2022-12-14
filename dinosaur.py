



#Dino class and characteristics
class Dinosaur:
    def __init__ (self, dino_name, health, attack):
        self.name = dino_name
        self.health = health
        self.attack_power = attack
        pass

    #set attack methods causes health loss 
    def attack(self, robot):
        robot.health -= self.attack_power
        print(f"{self.name} has attacked {robot.name} for {self.attack_power} damage leaving {robot.name} with {robot.health} remaining.")
        


    

