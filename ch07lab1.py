import pygame
import random

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
win = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption('KEY EVENT')

clock = pygame.time.Clock()


class Box:
    def __init__(self):
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT // 2
        self.size = 20
        self.color = 'green'
        self.speed = 5
        self.rect = pygame.Rect(0, 0, 0, 0)



    def move_up(self):
        if self.y > 0:
            self.y -= self.speed

    def move_down(self):
        if self.y <SCREEN_HEIGHT - self.size:
            self.y += self.speed

    def move_left(self):
        if self.x > 0:
            self.x -= self.speed

    def move_right(self):
        if self.x <SCREEN_WIDTH - self.size:
            self.x += self.speed

    def draw(self):
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)
        pygame.draw.rect(win, self.color, self.rect)



box = Box()
box_r = Box()
box_r.x = random.randint(0, SCREEN_WIDTH - box_r.size)
box_r.y = -box_r.size
box_r.color = 'white'


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        box.move_up()
    if keys[pygame.K_s]:
        box.move_down()
    if keys[pygame.K_a]:
        box.move_left()
    if keys[pygame.K_d]:
        box.move_right()

    box_r.move_down()
    if box_r.y > SCREEN_HEIGHT:
        box_r.y = -box_r.size
        box_r.x = random.randint(0, SCREEN_WIDTH - box_r.size)


    if box.rect.colliderect(box_r.rect):
        box.size -= 1
        box_r.y = -20
        box_r.x = random.randint(0, SCREEN_WIDTH - box_r.size)



    win.fill('black')
    box.draw()
    box_r.draw()
    pygame.display.update()
    clock.tick(60)

pygame.quit()