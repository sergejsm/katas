class Fighter(object):
    def __init__(self, name, health, damage_per_attack):
        self.name = name
        self.health = health
        self.damage_per_attack = damage_per_attack

    def __str__(self): return "Fighter({}, {}, {})".format(self.name, self.health, self.damage_per_attack)
    __repr__=__str__

def declare_winner(fighter1, fighter2, first_attacker):

    if fighter1.name == first_attacker:
        first = fighter1
        second = fighter2
    else:
        first = fighter2
        second = fighter1

    while True:
        second.health -= first.damage_per_attack
        if second.health <= 0:
            return first.name
        first.health -= second.damage_per_attack
        if first.health <= 0:
            return second.name


# print(declare_winner(Fighter("Lew", 10, 2),Fighter("Harry", 5, 4),"Lew"))  # Lew wins
print(declare_winner(Fighter("Jerry", 30, 3), Fighter("Harald", 20, 5), "Jerry"))

#Best Solutions:



from math import ceil
from operator import attrgetter


def declare_winner2(fighter1, fighter2, first_attacker):
    fighter1.turns = ceil(fighter1.health / float(fighter2.damage_per_attack))
    fighter2.turns = ceil(fighter2.health / float(fighter1.damage_per_attack))
    if fighter1.turns == fighter2.turns:
        return first_attacker
    return max(fighter1, fighter2, key=attrgetter('turns')).name

def declare_winner3(fighter1, fighter2, first_attacker):
    cur, opp = (fighter1, fighter2) if first_attacker == fighter1.name else (fighter2, fighter1)
    while cur.health > 0:
        opp.health -= cur.damage_per_attack
        cur, opp = opp, cur
    return opp.name
