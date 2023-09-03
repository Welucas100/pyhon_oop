class Vehicle:
    def start(self):
        print('준비')

    def stop(self):
        print('정지')

    def move(self):
        print('이동')

class Car(Vehicle):
    pass


class Bicycle(Vehicle):
    pass

v1 = Vehicle() #Vehicle 클래스를 사용해 v1객체 생성
v1.start()
v1.move()
v1.stop()

c1 = Car() # car 클래스를 사용해 c1객체 생성
#car 클래스는 vehicle 클래스를 상속바아 vehicle모든 매서드 사용가능
c1.start() 

b1 = Bicycle()# Bicycle 클래스를 사용해 b1객체 생성
b1.move()

#car 클래스를 사용해 c2객체를 생성하고
#move(), stop() 메서드를 실행

c2 = Car()
c2.move()
c2.stop()
