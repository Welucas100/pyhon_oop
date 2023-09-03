#ch02_lab1.py

class Calculator:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def add(self):
        res = self.n1 + self.n2
        return res

    def sub(self):
        res = self.n1 - self.n2
        return res

    def mul(self):
        res = self.n1 * self.n2
        return res
        
    def div(self):
        res = self.n1 / self.n2
        return res

cal = Calculator(3, 5)
r = cal.add()
print(f'{cal.n1} + {cal.n2} = {r}')
print(f'{cal.n1} - {cal.n2} = {cal.sub()}')
print(f'{cal.n1} * {cal.n2} = {cal.mul()}')
print(f'{cal.n1} / {cal.n2} = {cal.div()}')
