

class Robot:
    #robot characteristics
    def __init__ (self, robot_name, attack_weapon, robot_health):
        self.name = robot_name
        self.weapon = attack_weapon
        self.health = robot_health
        

    #set been attack method causes health loss 
    def robot_attack(self, dino_health):
        self.attack -= dino_health
        print("The robot just attacked the dinosaur.")

#end    
