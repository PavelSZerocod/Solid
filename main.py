from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self, damage):
        pass

class Sword(Weapon):
    def __init__(self, name):
        self.name = name
    def attack(self, damage):
        print(f"Меч-кладенец наносит {damage} урона")

    def __str__(self):
        return self.name

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


sword = Sword("Меч-кладенец")
bow = Bow("Лук - разящий")

fighter = Fighter("Конан", sword)
monster = Monster("Горгулия")


print(f"{fighter} выбирает {bow}")
print(f"{fighter} наносит удар {bow}")
bow.attack(30)
print(f"Монстр {monster} погибает")


print(f"{fighter} выбирает {sword}")
print(f"{fighter} наносит удар {sword}")
sword.attack(50)
print(f"Монстр {monster} погибает")











