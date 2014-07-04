#!/usr/bin/python3
from functools import total_ordering


@total_ordering
class Item:
    def __init__(self, id, add, mult, name='No name'):
        self.id, self.add, self.mult, self.name = id, add, mult, name

    def __eq__(self, other):
        return self.mult == other.mult and self.add == other.add

    def __lt__(self, other):
        return (self.mult, self.add) < (other.mult, other.add)

    def __and__(self, other):
        sm, sa, om, oa = self.mult, self.add, other.mult, other.add
        return 0 if om == sm else (sm * sa - om * oa) / (om - sm)

    def __str__(self):
        return '{:s}: +{:d}, *{:d}%'.format(self.name, self.add, int(100 * self.mult))


weapons = [
    Item(1, 5, 1.00, 'Dagger'),
    Item(2, 30, 1.10, 'Bowie Knife'),
    Item(3, 10, 1.35, 'Kuhkuri Knife'),
    Item(4, 120, 1.25, 'Iron Sword'),
    Item(5, 380, 1.30, 'Bronze Sword'),
    Item(6, 1100, 1.35, 'Iron Axe'),
    Item(7, 850, 1.60, 'Steel Sword'),
    Item(8, 3000, 1.40, 'Steel Axe'),
    Item(9, 1400, 1.70, 'Broad Sword'),
    Item(10, 2300, 1.75, 'Francisca'),
    Item(11, 1100, 2.25, 'Scimitar'),
    Item(12, 5000, 1.45, 'Battle Axe'),
    Item(13, 2700, 1.80, 'Glaive'),
    Item(14, 1800, 2.30, 'Trident'),
    Item(15, 1000, 2.50, 'Wind Sword'),
    Item(16, 1300, 2.70, 'Wind Sword+1'),
    Item(17, 200, 2.20, 'Fire Sword'),
    Item(18, 2600, 2.40, 'Fire Sword +1'),
    Item(19, 600, 2.70, 'Ice Sword'),
    Item(20, 800, 2.90, 'Ice Sword+1'),
    Item(21, 150, 2.90, 'Thunder Sword'),
    Item(22, 180, 3.10, 'Thunder Sword+1'),
    Item(23, 1700, 2.60, 'Silver Sword'),
    Item(24, 1600, 2.80, 'Silver Spear'),
    Item(25, 5000, 2.25, 'Samurai Sword'),
    Item(26, 2000, 2.60, 'Dark Sword'),
    Item(27, 9000, 1.30, 'Dark Axe'),
    Item(28, 500, 2.90, 'Rare Sword'),
    Item(29, 50, 3.30, 'Rare Gladius'),
    Item(30, 1600, 2.90, 'Knight Sword'),
    Item(31, 250, 3.40, 'Knight Rapier'),
    Item(32, 3500, 2.80, 'Knight Spear'),
    Item(33, 33000, 1.10, 'Tomahawk'),
    Item(34, 11000, 2.25, 'Samurai Long Sword'),
    Item(35, 0, 3.50, 'Estoc'),
    Item(36, 0, 3.75, 'Estoc+1'),
    Item(37, 7000, 2.30, 'Mace'),
    # Item(38, 3000, 2.90, 'Hard Sword'),
    Item(39, 10000, 2.20, 'Hard Axe'),
    # Item(40, 5000, 2.80, 'Hard Lance'),
    # Item(41, 5000, 3.30, 'Gold Sword'),
    # Item(42, 18000, 2.00, 'Gold Axe'),
    Item(43, 3000, 3.70, 'Green Light Sword'),
    # Item(44, 6000, 3.20, 'Red Light Sword'),
    Item(45, 15000, 2.90, 'Crystal Hammer'),
    # Item(46, 15000, 3.65, 'Four gods/Red Lance'),
    # Item(47, 1400, 3.00, 'Lvateinn/Cursed Sword'),
    # Item(48, 60, 3.50, 'Kujang/Cursed Sword'),
    # Item(49, 16000, 2.00, 'Durandal/Cursed Axe'),
    # Item(50, 4000, 2.90, 'GaeBolg/Cursed Lance'),
    # Item(51, 9000, 3.20, 'Excalibur/Holy Sword'),
    # Item(52, 24000, 1.60, 'Swanchika/Holy Axe'),
    # Item(53, 3000, 3.80, 'Longinus/Holy Lance'),
]
armor = [
    Item(1, 5, 1.00, 'Leather'),
    Item(2, 40, 1.10, 'Iron'),
    Item(3, 200, 1.25, 'Bronze'),
    Item(4, 530, 1.40, 'Steel'),
    Item(5, 870, 1.45, 'Scale'),
    Item(6, 900, 1.60, 'Spike'),
    Item(7, 5, 2.80, 'Magic'),
    Item(8, 700, 2.10, 'Full Plate'),
    Item(9, 700, 2.50, 'Silver'),
    Item(10, 1400, 2.40, 'Samurai'),
    Item(11, 800, 2.35, 'Dark'),
    Item(12, 50, 3.20, 'Rare'),
    Item(13, 800, 2.80, 'Knight'),
    Item(14, 5000, 2.60, 'Half'),
    Item(15, 3500, 2.30, 'Hard'),
    Item(16, 2500, 3.20, 'Gold'),
    Item(17, 0, 3.40, 'Light'),
    Item(18, 7000, 2.90, 'Crystal Cape'),
    # Item(19, 12000, 3.25, 'Four gods/Green Armor'),
    Item(20, 1800, 3.00, 'Megin Gjord/Cursed'),
    # Item(21, 5000, 3.30, 'Aegis/Holy'),
]


def get_optimum(items):
    items = list(items)
    items.sort()
    top = items[-1]
    optimum = []
    marker = float('inf')
    while marker > 0:
        cross = 0
        new_top = None
        for item in items:
            if item < top:
                new_cross = item & top
                if new_cross > cross or (new_cross == cross and new_top and new_top > item):
                    cross = new_cross
                    new_top = item
        optimum.append((cross, marker, top))
        marker, top = cross, new_top
    optimum.reverse()
    return optimum


def print_optimum(optimum):
    for lower, upper, item in optimum:
        print('{:.0f}:{:.0f} -> {:s}'.format(lower, upper, item))

# print('Weapons List:')
# print(*weapons, sep='\n')
# print()
print('Weapons Picks:')
print_optimum(get_optimum(weapons))
print()
# print('Armor List:')
# print(*armor, sep='\n')
# print()
print('Armor Picks:')
print_optimum(get_optimum(armor))
