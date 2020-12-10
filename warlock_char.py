from character import Character

class Warlock(Character):
    CLASS_NAME = "Warlock"
    _SUBCLASSES = ["Voidwalker", "Sunsinger", "Stormcaller"]

    def addWeapon(self, Weapon):
        if Weapon.classCompatible(self.getClassName()):
            super().addWeapon(Weapon)
        else:
            print(f"Cannon add weapon: {Weapon.getClassExclusiveName()} exclusive")
