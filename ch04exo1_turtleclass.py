import turtle as t
import random

class Racer:
    def __init__(self, tt, col, y):
        self.tt = tt
        self.speed = random.randint(2, 10)
        self.finish = False

        # 거북이 설정 초기화
        self.tt.shape('turtle')
        self.tt.color(col)
        self.tt.speed(0)
        self.tt.up()
        self.tt.goto(-250, y)

    def move(self):
        self.tt.forward(self.speed)
        if self.tt.xcor() > 250:
            self.finish = True



t.setup(600, 400)
t.bgcolor('orange')


# 경주
rt = t.Turtle()
bt = t.Turtle()
gt = t.Turtle()

red_turtle = Racer(rt, 'red', 50)
blue_turtle = Racer(bt, 'blue', 0)
green_turtle = Racer(gt, 'green', -50)

while not red_turtle.finish and not blue_turtle.finish and not green_turtle.finish:
    red_turtle.move()
    blue_turtle.move()
    green_turtle.move()


t.done()