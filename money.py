class Money:
    amount = 1

    def __init__(self, amount):
        self.amount = amount

    def __eq__(self, other):
        return self.amount == other.amount and type(self) == type(other)

    @staticmethod
    def dollar(amount):
        return Dollar(amount)

    @staticmethod
    def franc(amount):
        return Franc(amount)


class Dollar(Money):
    def times(self, multiple):
        return Dollar(self.amount * multiple)


class Franc(Money):
    def times(self, multiple):
        return Franc(self.amount * multiple)
