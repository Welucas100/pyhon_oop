import pygame

pygame.init()


SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
win = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption('pygame')

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    win.fill('black')


    r1 = pygame.Rect(150, 170, 300, 100)
    pygame.draw.rect(win, 'white', r1)
    r2 = pygame.Rect(230, 100, 140, 100)
    pygame.draw.rect(win, 'white', r2)
    r3 = pygame.Rect(265, 120, 70, 50)
    pygame.draw.rect(win, 'blue', r3)

    pygame.draw.circle(win, 'gray', (230, 270), 30)
    pygame.draw.circle(win, 'gray', (350, 270), 30)

    pygame.display.update()
