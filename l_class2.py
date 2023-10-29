import random

import pygame

pygame.init()

# 창 생성
WIN_WIDTH = 400
WIN_HEIGHT = 600
WIN_SIZE = (WIN_WIDTH, WIN_HEIGHT)
win = pygame.display.set_mode(WIN_SIZE)
pygame.display.set_caption('BOX ATTACK')

clock = pygame.time.Clock()

# 플레이어 클래스
class Player:
    def __init__(self):
        self.size = 20
        self.speed = 5
        self.x = WIN_WIDTH // 2
        self.y = WIN_HEIGHT - self.size
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)

    def move_left(self):
        if self.x > 0:
            self.x -= self.speed

    def move_right(self):
        if self.x < WIN_WIDTH - self.size:
            self.x += self.speed

    def draw(self):
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)
        pygame.draw.rect(win, 'yellow', self.rect)


# 미사일 클래스
class Bullets:
    def __init__(self):
        self.size = 10
        self.speed = 10
        self.x = player.x + player.size // 2 - self.size // 2
        self.y = player.y
        self.remove = False
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)

    def move(self):
        self.y -= self.speed
        if self.y < 0:
            self.remove = True

    def draw(self):
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)
        pygame.draw.ellipse(win, 'orange', self.rect)

class Box:
    def __init__(self):
        self.size = 20
        self.speed = 5
        self.x = random.randint(0, WIN_WIDTH - self.size)
        self.y = random.randint(-self.size * 10, -self.size)
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)
        self.remove = False

    def move(self):
        self.y += self.speed
        if self.y > WIN_HEIGHT:
            self.remove = True

    def draw(self):
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)
        pygame.draw.rect(win, 'green', self.rect)

# 게임 초기화
player = Player()
bullets = []
boxes = [Box()]
box_time = pygame.time.get_ticks()
bullet_time = pygame.time.get_ticks() # 현 시간 측정

# 반복 구문
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]:
        player.move_left()
    if pressed[pygame.K_RIGHT]:
        player.move_right()

    if pressed[pygame.K_SPACE]:
        current_time = pygame.time.get_ticks()
        if current_time - bullet_time > 100:
            bullet_time = current_time
            bullets.append(Bullets())

    current_time = pygame.time.get_ticks()
    if current_time - box_time > 500:
        box_time = current_time
        boxes.append(Box())

    for bullet in bullets:
        bullet.move()
        for box in boxes:
            if box.rect.colliderect(bullet.rect):
                box.remove = True
                bullet.remove = True
        if bullet.remove:
            bullets.remove(bullet)

    for box in boxes:
        box.move()
        if box.remove:
            boxes.remove(box)

    win.fill('black')

    player.draw()
    for bullet in bullets:
        bullet.draw()
    for box in boxes:
        box.draw()
    pygame.display.update()

    clock.tick(60)

pygame.quit()