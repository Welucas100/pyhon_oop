import pygame
import random


# 파이게임 초기화
pygame.init()



# 창 생성
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

win = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption('Eat it!')

# 클럭 설정
clock = pygame.time.Clock()

image_strawberry = pygame.image.load('food_strawberry.png')
image_watermelon = pygame.image.load('food_watermellon.png')
image_cake = pygame.image.load('food_cake.png')
image_background = pygame.image.load('background.png')

class Player:
    def __init__(self):
        self.x = 20
        self.image = pygame.image.load('player.png')
        #self.image = pygame.transform.scale(self.image, (300, 300))
        self.y = SCREEN_HEIGHT / 2 - self.image.get_height() / 2
        self.speed = 5
        self.chance = 5
        self.rect = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())

    def draw(self):
        self.rect = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())
        win.blit(self.image, (self.x, self.y))

    def move_up(self):
        if self.y >= 0:
            self.y -= self.speed

    def move_down(self):
        if self.y <= SCREEN_HEIGHT - self.image.get_height():
            self.y += self.speed

class Food:
    def __init__(self):
        idx = random.randint(0, 2)
        self.image = [image_strawberry, image_watermelon, image_cake][idx]
        self.x = random.randint(SCREEN_WIDTH, SCREEN_WIDTH + 150)
        self.y = random.randint(0, SCREEN_HEIGHT - self.image.get_height())
        self.speed = [3, 5, 7][idx]
        self.point = [10, 20, 30][idx]
        self.destroy = False
        self.rect = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())

    def move(self):
        self.x -= self.speed
        if self.x < 0:
            self.destroy = True

    def draw(self):
        win.blit(self.image, (self.x, self.y))
        self.rect = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())

score = 0

player = Player()
foods = [Food()]
start_time = pygame.time.get_ticks()
game_font = pygame.font.SysFont('D2Coding', 20)


# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.chance -= 1
                foods = []
                if player.chance < 1:
                    pygame.time.wait(2000)
                    running = False


    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        player.move_up()
    if pressed[pygame.K_DOWN]:
        player.move_down()


    if pygame.time.get_ticks() - start_time > 3000:
        start_time = pygame.time.get_ticks()
        foods.append(Food())


    for one in foods:
        one.move()
        if one.rect.colliderect(player.rect):
            one.destroy = True
            score += one.point
        if one.destroy:
            foods.remove(one)
            foods.append(Food())
            if one.x < 20:
                player.chance -= 1
                if player.chance == 0:
                    pygame.time.wait(2000)
                    running = False


    win.blit(image_background, (0, 0))
    for one in foods:
        one.draw()
    player.draw()
    score_text = game_font.render(f'SCORE: {score}', True, 'yellow')
    chance_text = game_font.render(f'chance: {player.chance}', True, 'yellow')
    win.blit(score_text, (20, 20))
    win.blit(chance_text, (500, 20))
    pygame.display.update()
    clock.tick(60)


# 파이게임 종료
pygame.quit()