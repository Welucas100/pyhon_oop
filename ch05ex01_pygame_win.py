import pygame

# 파이게임 초기화
pygame.init()

# 창 생성
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

win = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption('PYGAME')

# 반복 구문
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


# 파이게임 종료
pygame.quit()



