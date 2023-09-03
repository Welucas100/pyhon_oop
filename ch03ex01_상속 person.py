#ch03ex02_상속 person.py

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        msg = f'{self.name}은 {self.age}살 입니다.'
        return msg

    def intro(self):
        print(f'이름 : {self.name}')
        print(f'나이: {self.age}')

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        msg = f'{self.name}은 {self.age}살 입니다.'
        return msg

    def intro(self):
        print(f'이름: {self.name}')
        print(f'나이: {self.age}')
        print('직업: 학생')

class Bizman:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        msg = f''
        return msg
    def intro(self):
        print(f'이름: {self.name}')
        print(f'나이: {self.age}')
        print('직업: 회사원')
#홍길동, 999살 person 생성 후 출력

person1 = Person('홍길동', 999)
person1.intro()
print(person1)

st1 = Student('김철수', 15)
st1.intro()
print(st1)



print('-'*30)
b1 = Bizman('박출근', 30)
b1.intro()
print(b1)









