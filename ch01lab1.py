#ch01lab.1py

class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result
    def sub(self, num):
        self.result -= num
        return self.result
    def mul(self, num):
        self.result *= num
        return self.result
    def div(self, num):
        if num == 0:
            print('0으로 나눌 수 없습니다.')
            return self.result
        self.result /= num
        return self.result

n1 = Calculator()
r=n1.add(5)
print(f'+5==>{r}')
print(f'-2==>{n1.sub(2)}')
print(f'*3==>{n1.mul(2)}')
print(f'/2==>{n1.div(2)}')

#div매서드에 인자가 0인 경우 '0으로 나눌 수 없습니다.' 출력후
# 이전의 result값을 반환하도록 수정

r = n1.div(0)
print(r)
