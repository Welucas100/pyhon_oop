#ch02ex01_생성자 계산기.py

class Calculator: #class Calculator
    def __init__(self, n1, n2):
        self.n1=n1 #n1 속성 (property)
        self.n2= n2 # n2 속성

    def add(self): #add 메서드(method)
        r = self.n1 + self.n2
        return r

#두 속성 (3,5) 를 갖는 Calcultor 객체 cal1을 생성
cal1 = Calculator(3, 5)
res = cal1.add() #cal1 객체의 add 매서드 실행
print(f'cal1객체')
print(f'{cal1.n1} + {cal1.n2} = {res}') #3+5 = 8
cal1.n1 = 10
print(f'{cal1.n1} + {cal1.n2} = {res}') 
print('-' * 10)


cal2 = Calculator(5, 8)


res = cal2.add()
print(f'cal2객체')
print(f'{cal2.n1} + {cal2.n1} = {res}')
