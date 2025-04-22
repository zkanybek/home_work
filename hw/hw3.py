from hw.main import Hero

class Jester(Hero):
    def unique_atttack(self):
        print(f'{self.name} делает шутливую, но смертельную атаку! ')

    def unique_scream(self):
        print(f'{self.name} кричит: "Симейся пока можешь!"')

    def action(self):
        action_type = self.get_random_int()
        if action_type == 1:
            self.attack()
        elif action_type == 2:
            self.protection()
        elif action_type == 3:
            self.rest()