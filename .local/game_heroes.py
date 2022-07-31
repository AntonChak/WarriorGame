from game.weapon_quality import rare, improved
from base_classes import Warrior, Weapons
from game_weapons import Sword, Staff, Knife, Spear, Bow, Crossbow, Axe
from random import *
import time as t


class Hero(Warrior):
    def __init__(self, attack_counter=0, attack_punch=5):
        super().__init__(lvl=1, health=300, name='Unknown', defend=10, money=0)
        self.attack_counter = attack_counter
        self.attack_punch = attack_punch

    ''' Атака на моба '''

    def attack(self, other):
        rand = bool(randint(0, 1))
        if rand:
            other.health -= self.weapon.damage  #дамаге это атрибут оружия --урон оружия
            self.attack_counter += 1
            if self.attack_counter % 5 == 0:
                self.up_lvl()
            if other.health <= 0:
                print(f'{other.name} умер')
                print('игра закончилась')
            else:
                print(f'{self.name} наносит удар, {other.name} ранен, у противника осталось {other.health} здоровья')
        else:
            other.defend(self)

    '''Защита от атаки'''

    def defender(self, other):
        if other.lvl == self.lvl:
            print(f'{self.name} отразил удар')
        elif other.lvl > self.lvl:
            random_attack = randint(15, 20)
            self.health -= random_attack + self.defend
            print(f'уровень {other.name} больше твоего, получай ответный урон ==> {random_attack} ! остаток здоровья {self.name} = {self.health}')
        else:
            other.health -= self.weapon + other.defend
            self.attack_counter += 1
            if self.attack_counter % 5 == 0:
                self.up_lvl()

    ''' поднятие уровня '''

    def up_lvl(self):
        if self.lvl < 10:
            self.lvl += 1
            self.health += 55
            self.defend += 5

    ''' бабло с моба '''

    def death_in_battle(self, other):
        self.money += other.money

        self.weapon = Weapons.random_weapon()

    def add_weapon(self, another_weapon):
        if len(self.weapon) < 4:
            self.weapon.append(another_weapon)
            return True
        else:
            print('не можете взять оружие, рюкзак переполнен')
            return False


    # def change_weapon(self):
    #     if randint(0, 1) == 1:




