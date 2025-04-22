import random
from abc import ABC, abstractmethod

class Hero(ABC):
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.__random_int = random.randint(1, 3)

    def attack(self):
        print(f"{self.name} атакует врага!")

    def protection(self):
        print(f"{self.name} защищается!")

    def rest(self):
        self.health += 10
        print(f"{self.name} отдыхает и восстанавливает здоровье. Текущее здоровье: {self.health}")

    def get_random_int(self):
        return self.__random_int

    @abstractmethod
    def unique_attack(self):
        pass

    @abstractmethod
    def unique_scream(self):
        pass

    @abstractmethod
    def action(self):
        pass
