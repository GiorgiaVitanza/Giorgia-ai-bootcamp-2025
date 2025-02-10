class Account:
    def __init__(self, name):
        self.name = name
        self.balance = 0

    def deposit(self, money):
        self.balance = self.balance + money


gio = Account("Giorgia")
gio.deposit(500)
assert gio.balance == 500
