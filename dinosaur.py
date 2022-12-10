

class Dinosaur:
#Dino class and characteristics
    def __init__ (self, dino_name, attack_power, dino_health):
        self.name = dino_name
        self.power = attack_power
        self.health = dino_health
        
    #set attack methods causes health loss 
    def dino_attack(self, robot_health):
        self.attack -= robot_health
        print("The dino just attacked the robot.")

    
#end

