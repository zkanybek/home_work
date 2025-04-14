
from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def move(self):
        pass

class Dog(Animal):
    pass

    def make_sound(self):
        return "Gaf gaf"

    def move(self):
        return "action step"

dog = Dog()

print(dog)
print(dog.make_sound())
print(dog.move())
