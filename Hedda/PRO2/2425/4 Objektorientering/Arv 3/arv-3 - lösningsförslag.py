import random

def roll_dice(n, exploding = True, sides = 6):
    res = 0
    while n > 0:
        die = random.randint(1,sides)
        if die == sides and exploding:
            n += 1
            continue
        res += die
        n -= 1
    return res

class Item():

    def __init__(self, name, weight, bonus = [None, None]):
        self.name = name
        self.weight = weight
        self.bonus = bonus

class Armour(Item):

    def __init__(self, name, weight, defence, bonus = [None, None]):
        super().__init__(name, weight, bonus)
        self.defence = defence

class Weapon(Item):

    def __init__(self, name, weight, damage, bonus = [None, None]):
        super().__init__(name, weight, bonus)
        self.damage = damage

class Character():

    def __init__(self, name):
        self.name = name

        self.skills = {}
        self.weapon = None
        self.shield = None
        self.armour = None
        self.gold = 0
        self.health = 5
        self.gear = []
        self.encumbrance = 0
        
        self._calculate_encumbrance()

    def add_skill(self, skill, value = 0):
        self.skills[skill] = value

    def _calculate_encumbrance(self):
        self.encumbrance = 0
        if isinstance(self.weapon, Item):
            self.encumbrance += self.weapon.weight
        if isinstance(self.shield, Item):
            self.encumbrance += self.shield.weight
        if isinstance(self.armour, Item):
            self.encumbrance += self.armour.weight
        for item in self.gear:       
            if isinstance(gear, Item):
                self.encumbrance += gear.weight
        self.encumbrance += self.gold/10

    def _calculate_bonus(self, skill):
        bonus = self.skills[skill]
        for item in self.gear:
            if item.bonus[0] == skill:
                bonus += item.bonus[1]
        if isinstance(self.weapon, Item):
            if self.weapon.bonus[0] == skill:
                bonus += self.weapon.bonus[1]
        if isinstance(self.shield, Item):
            if self.shield.bonus[0] == skill:
                bonus += self.shield.bonus[1]
        if isinstance(self.armour, Item):
            if self.armour.bonus[0] == skill:
                bonus += self.armour.bonus[1]
        return bonus

    def add_gear(self, item):
        self.gear.append(item)
        self._calculate_encumbrance()

    def remove_gear(self, item):
        for i in range(len(self.gear)):
            if self.gear[i].name = item:
                self.gear.pop(i)
                break
        self._calculate_encumbrance()

    def add_gold(self, amount):
        self.gold += amount
        self._calculate_encumbrance()

    def attack(self):
        bonus = self._calculate_bonus("attack")
        res = roll_dice(self.skills["attack"]+bonus)
        return res
        
        
