import pygame

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
win = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption('pygame')

running = True
x = -10
r=0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 화면 지우기
    win.fill('black')


    # 사각형 그리기
    r1 = pygame.Rect(50, 50, 100, 100)
    pygame.draw.rect(win, 'yellow', r1, 5)
    r2 = pygame.Rect(50, 170, 150, 30)
    pygame.draw.rect(win, 'yellow', r2)
    r3 = pygame.Rect(170, 50, 30, 100)
    pygame.draw.rect(win, 'yellow', r3)

    # 타원 그리기
    pygame.draw.ellipse(win, 'red', r1, 5)
    pygame.draw.ellipse(win, 'red', r2)

    # 원 그리기
    pygame.draw.circle(win, 'green', (300,200), 50, 5)

    #다각형 그리기
    pygame.draw.polygon(win, 'aqua', [(400, 100), (500, 30), (550, 180)])

    #원그리기
    pygame.draw.circle(win, 'green', (x, 300), r)
    x+=0.1
    r+=0.1

    # 화면 갱신
    pygame.display.update()

pygame.quit()
