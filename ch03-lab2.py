#ch03-lab2.py

class Car:
    def __init__(self, car_type='normal', color='white', speed=80):
        self.car_type = car_type
        self.color = color
        self.speed = speed
        self.dist = 0

    def __str__(self):
        return f'{self.car_type}이고 색은{self.color}이고 속도는 {self.speed}이다.'

    def move_car(self):
        self.dist = self.dist + self.speed
        

class FastCar(Car):
    def __init__(self):
        super().__init__('sport', 'red', 100)
class TurboCar(Car):
    def __init__(self):
        super().__init__('Turbo', 'black', 300)


    
c1 = Car()
c2 = FastCar()
c3 = TurboCar()
c4 = Car('Ultra', 'yellow', 500)

print(c1)
print(c2)
print(c3)
print(c4)


for x in range(10):
    c1.move_car()
    c2.move_car()
    c3.move_car()
    c4.move_car()
    
    print(f'car: {c1.dist}, fast car: {c2.dist}, turbo car: {c3.dist}, ultra car:{c4.dist}')

print(c1.dist)
print(c2.dist)
print(c3.dist)



