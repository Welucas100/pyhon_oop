# 미사일 구현

import pygame

pygame.init()

WIN_WIDTH = 400
WIN_HEIGHT = 600
WIN_SIZE = (WIN_WIDTH, WIN_HEIGHT)
win = pygame.display.set_mode(WIN_SIZE)
pygame.display.set_caption('BULLET')

clock = pygame.time.Clock()

class Bullet:
    def __init__(self):
        self.size = 20
        self.speed = 10
        self.x = WIN_WIDTH // 2
        self.y = WIN_HEIGHT - self.size
        self.remove = False
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)

    def move(self):
        self.y -= self.speed
        if self.y < 0:
            self.remove = True

    def draw(self):
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)
        pygame.draw.rect(win, 'yellow', self.rect)


bullets = []  # 미사일 보관 리스트

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_SPACE]:
        bullets.append(Bullet())

    for bullet in bullets:
        bullet.move()


    win.fill("black")
    for bullet in bullets:
        bullet.draw()
    pygame.display.update()

    clock.tick(60)

pygame.quit()
