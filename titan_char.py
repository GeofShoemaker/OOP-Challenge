from character import Character

class Titan(Character):
    CLASS_NAME = "Titan"
    _SUBCLASSES = ["Striker", "Defender", "Sunbreaker"]

    def addWeapon(self, Weapon):
        if Weapon.classCompatible(self.getClassName()):
            super().addWeapon(Weapon)
        else:
            print(f"Cannon add weapon: {Weapon.getClassExclusiveName()} exclusive")

