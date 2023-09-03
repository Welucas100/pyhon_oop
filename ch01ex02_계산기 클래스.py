
#Calculator 클래스는 데이터(result)와 기능(add)로 구성된 클래스
#데이터: 속성(property), 필드(field)
#기능 : 메서드 (method)
class Calculator: 
    def __init__(self): #생성자
        self.result = 0 #self 객체 구분자
 
    def add(self, num): add메서드(num 매개변수)
        self.result += num
        return self.result

c1 = Calculator()
r= c1.add(5)
print(f'+5==>{r}')
r=c1.add(3)
print(f'+3 == > {r}')

#c2라는 계산기를 생성해 8을 더하고 출력, 2를 더하고 출력하시오.

c2 = Calculator()
r=c2.add(8) #c2객체에 add메서드에 인자를 8로 넣어 실행
print(f'+8==>{t}')
r=c2.add(2)
print(f'+2==>{t}')


r = c1.add(10)
print(f'c1: + 10== > {r}')
