#ch03ex01_상속 car.py

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def __str__(self):
        return f'brand: {self.brand}, model: {self.model}'

    def move(self):
        print(f'{self.model} Drive')

    #자동차 정보를 출력하는 intor()매서드 만들기

    def intro(self):
        print(f'브랜드: {self.brand}')
        print(f'모델: {self.model}')
        
class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def __str__(self):
        return f'brand: {self.brand}, model: {self.model}'

    def move(self):
        print(f'{self.brand} Sail')

    def intro(self):
        print(f'브랜드: {self.brand}')
        print(f'모델: {self.model}')
        


car1 = Car('tesla', 'model3')
print(car1)

#자동차 브랜드와 모델 출력해보기

print(car1.brand, car1.model)

car2 = Car('kia', 'canival')
car2.intro()
print(car2)

boat1 = Boat('Ibiza', 'Touring100')
print(boat1)
boat1.intro()
