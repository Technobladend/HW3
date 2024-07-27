class Bank:
    def __init__(self, name, balance=0):
        self._name = name
        self._balance = balance

    def moneyX(self):
        amount = int(input("Введите сумму: "))
        self._balance += amount
        return self._balance

    def _kill(self):
        self._balance = 0
        return self._balance

    def __jackpot(self):
        self._balance *= 10
        return self._balance

    def _balance_sum(self, other):
        self._balance += other._balance
        return self._balance
