class Weapon:
    def __init__(self, weapon_name, attack_power, damage):
        self.name = weapon_name
        self.attack = attack_power
        self.damage = damage
        
    def set_weapon(self, weapon_name, attack_power):
        self.weapon_name = weapon_name
        self.attack_power = attack_power

    