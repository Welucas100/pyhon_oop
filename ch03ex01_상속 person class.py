#ch03ex_상속 person calss.py

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def __str__(self):
        msg = f'{self.name}은 {self.age}살 입니다.'
        return msg
    def intro(self):
        print(f'이름: {self.name}')
        print(f'나이: {self.age}')

class Student(Person):
    def intro(self):
        super().intro()
        print(f'직업: 학생')

class Bizman(Person):
    def intro(self):
        super().intro()
        print(f'직업: 회사원')

p1 = Person('?', 10)
print(p1)
p1.intro()

s1 = Student('이승찬', 18)
print(s1)
s1.intro()

b1 = Bizman('김출근', 35)
print(b1)
b1.intro()
