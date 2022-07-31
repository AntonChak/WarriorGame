from random import randint, choice

from game.weapon_quality import rare, improved
from base_classes import Weapons

class BaseWeapon(Weapons):
    def weapon_repair(self):
        pass

    def enhancement(self):
        pass

    def random_weapon(self):
        pass


class Punch(BaseWeapon):
    def __init__(self):
        super().__init__(damage=10, weapon_strength=True)

    def __str__(self):
        return 'Кулаки'


class Sword(BaseWeapon):
    def __init__(self):
        super().__init__(damage=20, weapon_strength=20)

    def __str__(self):
        return "Меч"

class Spear(BaseWeapon):
    def __init__(self):
        super().__init__(damage=30,weapon_strength=20)

    def __str__(self):
        return "Пика"


class Knife(BaseWeapon):
    def __init__(self):
        super().__init__(damage=15,weapon_strength=20)

    def __str__(self):
        return "Нож"


class Bow(BaseWeapon):

    def __init__(self):
        super().__init__(damage=30,weapon_strength=20)

    def __str__(self):
        return "Лук"


class Crossbow(BaseWeapon):
    def __init__(self):
        super().__init__(damage=30, weapon_strength=20)

    def __str__(self):
        return "Арбалет"


class Staff(BaseWeapon):
    def __init__(self):
        super().__init__(damage=35,weapon_strength=20)

    def __str__(self):
        return "Посох"


class Axe(BaseWeapon):
    def __init__(self):
        super().__init__(damage=25,weapon_strength=20)

    def __str__(self):
        return "Топор"


def random_weapon():
    quality_weapon = ["ordinary", "rare", "improved"]
    weapon_list = [Sword, Staff, Knife, Spear, Bow, Crossbow, Axe]
    quality_random = choice(quality_weapon)
    weapon_random = choice(weapon_list)
    if quality_random == quality_weapon[0]:
        print('Обычное оружие:', weapon_random(),'урон', weapon_random().damage,'прочность',weapon_random().weapon_strength)
        return weapon_random()
    if quality_random == quality_weapon[1]:
        weapon = weapon_random()
        weapon.damage = weapon.damage * rare['damage']
        weapon.weapon_strength = weapon.weapon_strength * rare['weapon_strength']
        print('Редкое оружие:',weapon, 'урон', weapon.damage, 'прочность', weapon.weapon_strength)
        return weapon
    if quality_random == quality_weapon[2]:
        weapon = weapon_random()
        weapon.damage *= improved['damage']
        weapon.weapon_strength *= improved['weapon_strength']
        print('Улучшенное оружие:',weapon, 'урон', weapon.damage, 'прочность', weapon.weapon_strength)
        return weapon


c = random_weapon()
