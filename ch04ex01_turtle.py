import random
import turtle as t
import _random


# 이동 함수
def move():
    red_turtle.forward(red_turtle_speed)
    blue_turtle.forward(blue_turtle_speed)
    green_turtle.forward(green_turtle_speed)
    if red_turtle.xcor() < 250 and blue_turtle.xcor() < 250 and green_turtle.xcor() < 250:
        t.ontimer(move, 100)

    
# 창 설정
t.setup(600, 400)
t.bgcolor('orange')

# 빨강 거북이
red_turtle = t.Turtle()
red_turtle.shape('turtle')
red_turtle.color('red')
red_turtle.speed(0)
red_turtle.up()
red_turtle.goto(-250, 50)
red_turtle_speed = random.randint(2, 10)

# 파란 거북이
blue_turtle = t.Turtle()
blue_turtle.shape('turtle')
blue_turtle.color('blue')
blue_turtle.speed(0)
blue_turtle.up()
blue_turtle.goto(-250, -50)
blue_turtle_speed = random.randint(2, 10)

# 초록 거북이
green_turtle = t.Turtle()
green_turtle.shape('turtle')
green_turtle.color('green')
green_turtle.speed(0)
green_turtle.up()
green_turtle.goto(-250, 0)
green_turtle_speed = random.randint(2, 10)

# 이동
move()
# 창 유지
t.done()
