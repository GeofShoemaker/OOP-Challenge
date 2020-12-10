from weapon import Weapon

# This class is NOT meant to have any instances of it alone, to use, make child class object. Do NOT run from here.


class Character:
    # Subclasses
    _subclasses = []
    selected_subclass: int
    # Main inventory
    _primary_weapons: Weapon = []
    selected_primary: Weapon = None
    _special_weapons: Weapon = []
    selected_special: Weapon = None
    _heavy_weapons: Weapon = []
    selected_heavy: Weapon = None
    weapon_dict = {0: _primary_weapons, 1: _special_weapons, 2: _heavy_weapons}
    weapon_slot_link = {0: selected_primary,
                        1: selected_special, 2: selected_heavy}
    """
    #Haven't done this part yet -------------------
    _ghost_shells = []
    selected_shell = _ghost_shells[0]
    _helmets = []
    selected_helmet = _helmets[0]
    _gauntlets = []
    selected_gauntlet = _gauntlets[0]
    _leg_armor = []
    selected_leg_armor = _leg_armor[0]
    _boots = []
    selected_boots = _boots[0]
    _artifacts = []
    selected_artifact = _artifacts[0]
    # Secondary inventory
    _materials = []
    _consumables = []
    #-----------------------------------------------
    """
    # Currency
    _glimmer: int = 0
    _legendary_marks: int = 0

    # Levels
    light_level = 0
    level = 0
    
    # Compiled inventory (purely for my use atm)
    #inventory = [_primary_weapons, _special_weapons, _heavy_weapons, _ghost_shells, _helmets, _gauntlets, _leg_armor, _boots, _artifacts]
    # Class names for exclusive checks, meant to be overridden by the subclasses
    CLASS_NAME: str

    def __init__(self, selected_subclass: int = 0, glimmer: int = 0, legendary_marks: int = 0, light_level: int = 0, level: int = 0):
        self.selected_subclass = selected_subclass
        self._glimmer = glimmer
        self._legendary_marks = legendary_marks
        self.light_level = 0 if light_level < 0 else 400 if light_level > 400 else light_level
        self.level = 0 if level < 0 else 40 if level > 40 else level

    # Action methods
    def addWeapon(self, Weapon):
        weapon_list = self.weapon_dict[Weapon.getWeaponType()]
        if len(weapon_list) == 10:
            print("Cannot add weapon: storage full.")
        else:
            weapon_list.append(Weapon)
            print(f"{Weapon.name} added to inventory.")

    def dismantleWeapon(self, Weapon):
        weapon_list = self.weapon_dict[Weapon.getWeaponType()]
        equippedWeapon: type(Weapon)
        if weapon_list == self._primary_weapons:
            equipped_weapon = self.selected_primary
        elif weapon_list == self._special_weapons:
            equipped_weapon = self.selected_special
        else:
            equipped_weapon = self.selected_heavy
        if Weapon.getWeaponID() == equipped_weapon.getWeaponID():
            print("Cannont dismantle weapon: weapon is equipped.")
        else:
            for weapon in weapon_list:
                if (not weapon == None) and (weapon.getWeaponID() == Weapon.getWeaponID()):
                    self.addLegendaryMarks(weapon.dismantleLoot())
                    print(f"{Weapon.name} dismantled.")
                    del weapon_list[weapon_list.index(Weapon)]

    def equipPrimary(self, Weapon):
        try:
            self.selected_primary = self._primary_weapons[self._primary_weapons.index(
                Weapon)]
            print(f"{Weapon.name} equipped.")
        except:
            print(
                f"Cannot equip primary: You don't have {Weapon.name} in your primary weapon inventory.")

    def equipSpecial(self, Weapon):
        try:
            self.selected_special = self._special_weapons[self._special_weapons.index(
                Weapon)]
            print(f"{Weapon.name} equipped.")
        except:
            print(
                f"Cannot equip special: You don't have {Weapon.name} in your special weapon inventory.")

    def equipHeavy(self, Weapon):
        try:
            self.selected_heavy = self._heavy_weapons[self._heavy_weapons.index(
                Weapon)]
            print(f"{Weapon.name} equipped.")
        except:
            print(
                f"Cannot equip heavy: You don't have {Weapon.name} in your heavy weapon inventory.")

    def addGlimmer(self, glimmerToAdd: int = 1):
        self._glimmer += glimmerToAdd

    def addLegendaryMarks(self, marksToAdd: int = 1):
        self._legendary_marks += marksToAdd

    def levelUp(self):
        self.level += 1

    def lightLevelUp(self):
        self.light_level += 1

    # Getter methods
    def getLevel(self):
        return self.level

    def getLightLevel(self):
        return self.light_level

    def getClassName(self):
        return self.CLASS_NAME

    def getGlimmer(self):
        return self._glimmer

    def getLegendaryMarks(self):
        return self._legendary_marks

    # Helper methods
    def printPrimaryWeapons(self):
        for primary_weapon in self._primary_weapons:
            print(primary_weapon.getWeaponName())

    def printSpecialWeapons(self):
        for special_weapon in self._special_weapons:
            print(special_weapon.getWeaponName())

    def printHeavyWeapons(self):
        for heavy_weapon in self._heavy_weapons:
            print(heavy_weapon.getWeaponName())
