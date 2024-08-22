from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self, damage):
        pass

class Sword(Weapon):
    def __init__(self, damage):
        self.damage = damage

    def attack(self, damage):
        print(f"Меч-кладенец наносит {damage} урона")

class Bow(Weapon):
    def __init__(self, name):
        self.name = name
    def attack(self, damage):
        print(f"Лук-разящий наносит {damage} урона")

    def __str__(self):
        return self.name


class Fighter():
    def __init__(self, name, weapon:Weapon):
        self.name = name
        self.weapon = weapon

    def change_weapon(self, weapon:Weapon):
        self.weapon = weapon

    def attack(self, damage):
        self.weapon.attack(damage)

    def __str__(self):
        return self.name


class Monster():
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


sword = Sword("Меч-кладенец наносит")
bow = Bow(30)

fighter = Fighter("Конан", sword)
monster = Monster("Горгулия")

print(f"{fighter} выбирает {sword}")
print(f"{fighter} наносит удар {sword}")
print(f"Монстр {monster} погибает")











