class Hero:

    def __init__(self, name, lvl, hp):
        self.name = name #атрибуты
        self.lvl = lvl
        self.HP = hp

    def introduc(self):
        print(f'Привет, меня зовут {self.name}, мой lvl {self.lvl} , мое HP {self.HP}')
    def is_adult(self):
        if 10 <= self.lvl:
            return True
        else:
            return False


zk = Hero('zkanybek', 1, 100)
son = Hero('Son', 100, 1700)
black = Hero('Knight',9, 190 )

print(zk.introduc())
print(son.introduc())
print(black.introduc())

print(zk.is_adult())
print(son.is_adult())
print(black.is_adult())
