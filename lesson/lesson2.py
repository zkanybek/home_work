class Ban:
    def __init__(self, name, balance, password):
        self.namename = name
        self.balance = balance
        self.password = password

    def top_up_balance(self, amount):
        if amount > 0:
            self.balance += amount
            return
        else:
            return
