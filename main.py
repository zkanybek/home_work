
from random import random
from wsgiref.simple_server import server_version
import random

class Hero:
    def __init__ (self, attack, protection, rest):
        self.attack = attack
        self.protection = protection
        self.__random_int = self.__generate_random_int()

    def __generate_random_int(self):
        return random.randint(1,3)

    def get-



    def __random_int(self):
        import random
        random_namber = random.randint(1, 3)
        return random_namber

    # def  get_random_int(self):
    #     pass