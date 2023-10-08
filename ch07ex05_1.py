import pygame

pygame.init()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

win = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption('이벤트')

clock = pygame.time.Clock()

box_x = 200
box_y = 200
box_size = 20

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        box_size +=1
    if keys[pygame.K_DOWN]:
        box_size -=1
    if keys[pygame.K_w]:
        box_y -=1
    if keys[pygame.K_s]:
        box_y +=1
    if keys[pygame.K_a]:
        box_x -=1
    if keys[pygame.K_d]:
        box_x +=1

    win.fill('black')

    box_rect = pygame.Rect(box_x, box_y, box_size, box_size) # x, y, 가로길이, 세로길이

    box_rect.center = (box_x, box_y)
    pygame.draw.rect(win, 'yellow', box_rect)

    pygame.display.update()
    clock.tick(60)


pygame.quit()