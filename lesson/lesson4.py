from abc import ABC, abstractmethod

# class Math:
#     @staticmethod
#     def add(a, b):
#         return a + b
#
#     @classmethod
#     def info(cls):
#         return "Math class for simple calculations"
#
# class Person:
#     population = 0
#
#     def __init__(self, name):
#         self.name = name
#         Person.population += 1
#

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

circle = Circle(5)
print(circle.radius)


def my_dekorator(func):
    def wrapper():
        print("Перед выполнением функции")
        func()
        print("После выполнения функции")
    return wrapper

@my_dekorator
def hello():
    print("Привет")

# hello()

def repeat(n):
    def dekorator(func):
        def wrapper():
            for i in range(n):
                func()
        return wrapper
    return dekorator

amound = int(input("Enter number: "))

@repeat(amound)
def greet():
    print("hello")

greet()

