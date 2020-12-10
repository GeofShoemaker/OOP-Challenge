from character import Character
from weapon import Weapon


class Hunter(Character):
    CLASS_NAME = "Hunter"
    _SUBCLASSES = ["Gunslinger", "Bladedancer", "Nightstalker"]
    def addWeapon(self, Weapon):
        if Weapon.classCompatible(self.getClassName()):
            super().addWeapon(Weapon)
        else:
            print(f"Cannot add weapon: {Weapon.getClassExclusiveName()} exclusive.")
"""
my_char = Hunter()
gun = Weapon("Test Gun", 4, 1, 1, 1, 1, 1, 0, 1, 0, None)
gun2 = Weapon("Test Gun 2", 4, 1, 1, 1, 1, 1, 0, 1, 0, None)


my_char.addWeapon(gun)
my_char.addWeapon(gun2)
my_char.equipPrimary(gun)

my_char.dismantleWeapon(gun)
my_char.dismantleWeapon(gun2)

print(gun.getWeaponID())
print(gun2.getWeaponID())

print(gun.rarity)
print(gun.dismantleLoot)
print(my_char.getLegendaryMarks())"""
