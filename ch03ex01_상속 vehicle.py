#ch3ex01_상속 vehicle.py

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def __str__(self):
        return f'brand: {self.brand}, model: {self.model}'

    def intro(self):
        print(f'브랜드: {self.brand}')
        print(f'모델: {self.model}')
        
    def move(self):
        print(f'{self.model} Drive!')

class Car(Vehicle):
    def move(self):
        print(f'{self.model} Sail')

#boat class (이동 시 Sail! 출력)


class Boat(Vehicle):
    def move(self):
        print(f'{self.model} Sail!')

#plane class (이동 시 Fly! 출력)
class Plane(Vehicle):
    def move(self):
        print(f'{self.model} Fly!')

car1 = Car('현대', '아이오닉')
print(car1)
car1.intro()
car1.move()

plane1 = Plane('대한항공', '보잉747')
print(plane1)
plane1.intro()
plane1.move()

boat1 = Boat('이비자', '투어링20')
print(boat1)
boat1.intro()
boat1.move()
