# avoid_box.py

import pygame
import random

# pygame 최기화

pygame.init()

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
win = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption('박스 피하기')


clock = pygame.time.Clock()

# class 생성


class Box:
    def __init__(self):
        self.size = 20
        self.x = random.randint(0, SCREEN_WIDTH - self.size)
        self.y = random.randint(-150, -self.size)
        idx = random.randint(0, 2)
        self.color = ['green', 'orange', 'red'][idx]
        self.speed = [3, 7, 10][idx]
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)
        self.destroy = False

    def move(self):
        self.y += self.speed
        if self.y > SCREEN_HEIGHT:
            self.destroy = True

    def draw(self):
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)
        pygame.draw.rect(win, self.color, self.rect)


class Player(Box):
    def __init__(self):
        self.size = 20;
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT - self.size*2
        self.color = 'cyan'
        self.speed = 3
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)

    def move_left(self):
        if self.x > 0:
            self.x -= self.speed

    def move_right(self):
        if self.x < SCREEN_WIDTH - self.size:
            self.x += self.speed

# 게임 초기화
score = 0
chance = 3
game_over = False
player = Player()
boxes = []
for x in range(5):
    boxes.append(Box())
g_font = pygame.font.SysFont('D2Coding', 30)
b_time = pygame.time.get_ticks()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        # 키 입력
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]:
            player.move_left()
        if pressed[pygame.K_RIGHT]:
            player.move_right()

        if pygame.time.get_ticks() - b_time > 5000:
            b_time = pygame.time.get_ticks()
            boxes.append(Box())

        # 박스 이동
        for one in boxes:
            one.move()
            # 플레이어 충돌 화인 ( 충돌 시 destroy 실행)
            if player.rect.colliderect(one.rect):
                one.destroy = True
                chance -= 1
                if chance < 1:
                    game_over = True
                score -= 10
                if score < 0:
                    score = 0


            # 상자가 바닥에 닿으면 boxes에서 제거하고, 새로운 상자를 추가하기
            if one.destroy:
                boxes.remove(one)
                boxes.append(Box())
                score += 1
                if score % 100 ==0:
                    chance += 1


    # 화면 그리기

    win.fill('black')

    for one in boxes:
        one.draw()
    player.draw()
    score_text = g_font.render(f'SCORE: {score:05d}', True, 'white')
    win.blit(score_text, (20, 20))
    chance_text = g_font.render(f'CHANCE: {chance}', True, 'white')
    win.blit(chance_text, (SCREEN_WIDTH - 160, 20))
    pygame.display.update()
    clock.tick(60)

pygame.quit()