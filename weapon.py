from typing import Union
from id_generator import ID_Generator
import random as rng
class Weapon:
    RARITIES = {0: "Common", 1: "Uncommon", 2: "Legendary", 3: "Exotic"}
    DAMAGE_TYPES = {0: "Kinetic", 1: "Solar", 2: "Arc", 3: "Void"}
    WEAPON_TYPES = {0: "Primary", 1: "Special", 2: "Heavy"}

    def __init__(self, name: str, rarity: int, fire_rate: int, impact: int, damage_range: int, stability: int, reload_rate: int, damage_type: int, light_level: int, weapon_type: int, class_exclusive: Union[str, None]=None):
        self.name = name
        self.rarity = 3 if rarity > 3 else 0 if rarity < 0 else rarity
        self.weapon_type = 2 if weapon_type > 2 else 0 if weapon_type < 0 else weapon_type
        self.fire_rate = fire_rate
        self.impact = impact
        self.damage_range = damage_range
        self.stability = stability
        self.reload_rate = reload_rate
        self.damage_type = 3 if damage_type > 3 else 0 if damage_type < 0 else damage_type
        self.light_level = 400 if light_level > 400 else 0 if light_level < 0 else light_level
        self.class_exclusive = class_exclusive
        self.WEAPON_ID = ID_Generator.generateID()

    
    def getWeaponID(self):
        return self.WEAPON_ID

    def getWeaponName(self):
        return self.name

    def getWeaponType(self):
        return self.weapon_type

    def classCompatible(self, class_name):
        return self.class_exclusive == None or self.class_exclusive == class_name

    def getClassExclusiveName(self):
        return self.class_exclusive

    def dismantleLoot(self):
        return 0 if self.rarity < 2 else rng.randint(3, 5)


"""print(gun.rarities[gun.rarity])
print(gun.dismantleLoot())"""
