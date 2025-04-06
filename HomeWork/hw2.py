import random

class Heroes:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def ability(self, damage):
        if damage > 0:
            self.hp -= damage
            print(f"{self.name} получил урон: {damage}. Осталось HP: {self.hp}")
        else:
            print(f"{self.name} не получил урона.")

class Archer(Heroes):
    def __init__(self, name, hp, arrows=12, precision=50):
        super().__init__(name, hp)
        self.arrows = arrows
        self.precision = precision
        self.accuracy = 0.60

    def ability(self, damage):
        if self.arrows > 0:
            self.arrows -= 1  # Уменьшаем количество стрел
            if random.random() <= self.accuracy:
                print(f"{self.name} успешно атаковал! Нанесено урона: {damage}. Осталось стрел: {self.arrows}")
            else:
                print(f"{self.name} промахнулся! Осталось стрел: {self.arrows}")
        else:
            print(f"{self.name} не может атаковать, нет стрел!")

    def rest(self):
        self.arrows += 5
        print(f"{self.name} пополнил стрелы! Теперь у него {self.arrows} стрел.")

    def status(self):
        print(f"Имя: {self.name}\nЗдоровье: {self.hp}\nСтрелы: {self.arrows}\nТочность: {self.precision}%")

# Создание лучника
archer = Archer("Son", 100)

# Проверка методов
archer.status()
archer.ability(20)
archer.ability(15)
archer.status()
archer.rest()
archer.status()
