#ch03ex03_상속 super().py

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name}은 {self.age}살 입니다.'

class Bizman(Person):
    def __init__(self, name, age, dp):
        super().__init__(name, age)
        self.dp = dp

    def __str__(self):
        msg = super().__str__()
        msg2 = f'{self.dp} 부서에 근무 중 입니다.'
        return msg + '\n' + msg2

class Student(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject 

    def __str__(self):
        msg = super().__str__()
        msg2 = f'{self.subject}를 다니고 있다.'
        return msg + '\n' + msg2
        

p1 = Person('홍길동', 999)
p2 = Bizman('김출근', 33, '개발부')
p3 = Bizman('박퇴근', 55, '영업부')
p4 = Student('최철수', 19, '소프트웨어공학')
p5 = Student('장발장', 20, '경영학')
print(p1)
print(p2)
print(p3)
print(p4)
print(p5)
