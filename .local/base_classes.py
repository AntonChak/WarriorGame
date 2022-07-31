from abc import ABC, abstractmethod
from random import *
import time as t
from game_weapons import Punch,Weapons

class Warrior(ABC):
    def __init__(self, lvl=1, health=300, name='Unknown', defend=10, money=0):
        self.weapon = [Punch]
        self.health = health
        self.name = name
        self.defend = defend
        self.money = money
        self.lvl = lvl

    '''декоратор, который обязывает создавать декорируемый метод во всех дочерних классах'''

    @abstractmethod
    def attack(self, other):
        pass

    '''Защита от атаки'''

    @abstractmethod
    def defender(self, other):
        pass

    @abstractmethod
    def death_in_battle(self, other):
        pass



class Weapons(ABC):
    def __init__(self, damage, weapon_strength):
        self.damage = damage
        self.weapon_strength = weapon_strength

    @abstractmethod
    def weapon_repair(self):
        pass

    @abstractmethod
    def enhancement(self):
        pass

    @abstractmethod
    def random_weapon(self):
        pass