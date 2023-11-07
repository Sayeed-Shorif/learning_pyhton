class Money:
    def __init__(self, amount = 0):
        self.money = amount
        

    def payment(self, amount):
        if amount > self.money:
            return amount - self.money
        elif amount == self.money:
            return None
        else:
            return "Not enough money !"
m = Money()