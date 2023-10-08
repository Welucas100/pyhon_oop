import pygame

pygame.inti()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

win = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption('이벤트')

running = True
while running:
    for event in pygame.event.get()
        if event.type == pygame.QUIT:
            running = False

    box_rect = pygame.Rect(200, 200, 20, 20)
    pygame.draw.rect(win, 'yellow', boc_rect)


    pygame.display.update()


pygame.quit()