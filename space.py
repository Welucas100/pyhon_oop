# space 슈팅 게임

import pygame
import random

pygame.init()  # 파이게임 초기화

# 창 생성
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
win = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption('SPACE')

clock = pygame.time.Clock()

# 스프라이트 이미지 수 설정
space_image_num = 3
booster_image_num = 2
alan_image_num = 6
bon_image_num = 4
lips_image_num = 5
beam_image_num = 2
sparkle_image_num = 4
bg_image_num = 2

# 스프라이트 불러오기
alan_image = pygame.image.load('MiniPixel3/Enemies/Alan (16 x 16).png')
space_image = pygame.image.load('MiniPixel3/Player ship/Player_ship (16 x 16).png')
booster_image = pygame.image.load('MiniPixel3/Player ship/Boosters (16 x 16).png')
booster_left_image = pygame.image.load('MiniPixel3/Player ship/Boosters_left (16 x 16).png')
booster_right_image = pygame.image.load('MiniPixel3/Player ship/Boosters_right (16 x 16).png')
bon_image = pygame.image.load('MiniPixel3/Enemies/Bon_Bon (16 x 16).png')
lips_image = pygame.image.load('MiniPixel3/Enemies/Lips (16 x 16).png')
beam_image = pygame.image.load('MiniPixel3/Projectiles/Player_charged_beam (16 x 16).png')
sparkle_image = pygame.image.load('MiniPixel3/Effects/Sparkle (16 x 16).png')
bg_image = pygame.image.load('MiniPixel3/Space_BG (2 frames) (64 x 64).png')
game_over_image = pygame.image.load('MiniPixel3/UI objects/GAME_OVER (72 x 8).png')
game_over_image = pygame.transform.scale(game_over_image, (game_over_image.get_width() * 3, game_over_image.get_height() * 3))



# 스프라이트 분할
def split_sprite(sprite_image, split_num, scale = 2):
    sprite_scale = scale
    frames = []
    frame_width = sprite_image.get_width() // split_num
    frame_height = sprite_image.get_height()
    for i in range(split_num):
        frame = sprite_image.subsurface(pygame.Rect(i * frame_width, 0, frame_width, frame_height))
        frame = pygame.transform.scale(frame, (frame.get_width() * sprite_scale, frame.get_height() * sprite_scale))
        frames.append(frame)
    return frames


space_image = split_sprite(space_image, space_image_num)
bon_image = split_sprite(bon_image, bon_image_num)
lips_image = split_sprite(lips_image, lips_image_num)
booster_image = split_sprite(booster_image, booster_image_num)
booster_left_image = split_sprite(booster_left_image, booster_image_num)
booster_right_image = split_sprite(booster_right_image, booster_image_num)
booster_images = (booster_left_image, booster_image, booster_right_image)
alan_image = split_sprite(alan_image, alan_image_num)
beam_image = split_sprite(beam_image, beam_image_num)
sparkle_image = split_sprite(sparkle_image, sparkle_image_num)
bg_image = split_sprite(bg_image, bg_image_num, 3)

# 배경 초기화
bg_idx = 0
bg_width = bg_image[bg_idx].get_width()
bg_height = bg_image[bg_idx].get_height()
bg_num_x = SCREEN_WIDTH // bg_width + 1
bg_num_y = SCREEN_HEIGHT // bg_height + 1
bg_time = pygame.time.get_ticks()



# Space Class
class Space:
    LEFT = 0 # 클래스 변수
    CENTER = 1
    RIGHT = 2

    def __init__(self):
        self.life = 3
        self.image = space_image    # 인스턴스 변수
        self.idx = Space.CENTER     # 클래스 변수 Space 클래스의 CENTER 변수
        self.booster_image = booster_images[self.idx]
        self.booster_image_idx = 0
        self.booster_time = pygame.time.get_ticks()
        self.size = self.image[self.idx].get_width()
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT - self.size * 2
        self.speed = 3
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)   # pygame Rect에는 충돌을 확인하는 함수 colliderect 사용 가능

    def move_left(self):
        self.idx = Space.LEFT
        if self.x > 0:
            self.x -= self.speed


    def move_right(self):
        self.idx = Space.RIGHT
        if self.x < SCREEN_WIDTH - self.size:
            self.x += self.speed

    def draw_life(self):
        for i in range(self.life):
            win.blit(self.image[Space.CENTER], (270 + self.size * i + 10 * i, 10))

    def draw(self):
        # space 그리기
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)
        win.blit(self.image[self.idx], (self.x, self.y))
        # booster 그리기
        self.booster_image = booster_images[self.idx]
        win.blit(self.booster_image[self.booster_image_idx], (self.x, self.y + self.size))
        if pygame.time.get_ticks() - self.booster_time > 50:
            self.booster_time = pygame.time.get_ticks()
            self.booster_image_idx += 1
            if self.booster_image_idx >= booster_image_num:
                self.booster_image_idx = 0
# Beam Class
class Beam:
    def __init__(self):     # 생성자는 객체 생성 시 자동으로 호출되는 함수
        self.x = game.space.x
        self.y = game.space.y
        self.speed = 10
        self.img_idx = 0
        self.image = beam_image[self.img_idx]
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.remove = False

    def move(self):
        self.y -= self.speed
        if self.y < 0:
            self.remove = True

    def draw(self):
        self.image = beam_image[self.img_idx]
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        win.blit(self.image, (self.x, self.y))

# Enemy Class
class Enemy:
    def __init__(self, enemy_image, image_num, speed, update_time):
        self.update_time = update_time
        self.image = enemy_image
        self.num = image_num
        self.idx = 0
        self.size = self.image[self.idx].get_width()
        self.x = random.randint(0, SCREEN_WIDTH - self.size)
        self.y = -self.size
        self.speed = speed
        self.time = pygame.time.get_ticks()
        self.remove = False
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)

    def move(self):
        self.y += self.speed
        if self.y > SCREEN_HEIGHT:
            self.remove = True

    def draw(self):
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)
        win.blit(self.image[self.idx], (self.x, self.y))
        if pygame.time.get_ticks() - self.time > self.update_time:
            self.time = pygame.time.get_ticks()
            self.idx += 1
            if self.idx >= self.num:
                self.idx = 0



# Alan(Enemy) Class
class Alan(Enemy):
    def __init__(self):
        super().__init__(alan_image, alan_image_num, 3, 50)

    def move(self):
        if game.score > 100:
            self.x += random.choice([1, -1, 2, -2, 3, -3, 5, -5])
        super().move()

# Bon(Enemy) Class
class Bon(Enemy):
    def __init__(self):
        self.sx = 10
        super().__init__(bon_image, bon_image_num, 1, 80)

    def move(self):     # method overriding 메소드 오버라이딩
        self.x += self.sx
        if self.x > SCREEN_WIDTH or self.x < 0:
            self.sx *= -1
            self.y += self.size

# Lips(Enemy) Class
class Lips(Enemy):
    def __init__(self):
        super().__init__(lips_image, lips_image_num, 4, 50)

    def move(self):
        if game.score > 500:
            if self.x - game.space.x < 0:
                self.x += 1
            else:
                self.x -= 1
        super().move()

# Explode Class
class Sparkle:
    def __init__(self, sx, sy):
        self.x = sx
        self.y = sy
        self.img_idx = 0
        self.image = sparkle_image[self.img_idx]
        self.time = pygame.time.get_ticks()
        self.remove = False

    def draw(self):
        self.image = sparkle_image[self.img_idx]
        win.blit(self.image, (self.x, self.y))
        if pygame.time.get_ticks() - self.time > 50:
            self.img_idx += 1
            self.time = pygame.time.get_ticks()
            if self.img_idx > sparkle_image_num - 1:
                self.img_idx = 0
                self.remove = True

offset = 0
def draw_bg():
    global offset
    global bg_time, bg_idx
    for y in range(-1, bg_num_y + 1):
        for x in range(bg_num_x):
            win.blit((bg_image[bg_idx]), (x * bg_width, y * bg_height + offset))
    offset += 1
    if offset > bg_height:
        offset = 0
    if pygame.time.get_ticks() - bg_time > 100:
        bg_time = pygame.time.get_ticks()
        bg_idx += 1
        if bg_idx > bg_image_num - 1:
            bg_idx = 0

class Game:
    def __init__(self):
        self.running = True
        self.game_over = False
        self.space = Space()  # 우주선 객체 생성
        self.sparkles = []
        self.beams = []  # 미사일 초기화
        self.enemy = [random.choice([Alan(), Bon(), Lips()])]
        self.enemy_add_time = pygame.time.get_ticks()
        self.ENEMY_TIME = 300
        self.score = 0

    def key_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYUP:
                self.space.idx = Space.CENTER
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.beams.append(Beam())

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]:
            self.space.move_left()
        if pressed[pygame.K_RIGHT]:
            self.space.move_right()
        if game.game_over:
            if pressed[pygame.K_y]:
                self.__init__()

    def check_beam(self):
        for beam in self.beams:
            beam.move()
            # 충돌 처리
            for x in self.enemy:
                if beam.rect.colliderect(x.rect):
                    self.score += 10
                    if self.score % 100 == 0:
                        if self.ENEMY_TIME >= 100:
                            self.ENEMY_TIME -= 10

                    self.sparkles.append(Sparkle(x.x, x.y))
                    beam.remove = True
                    x.remove = True
            if beam.remove:
                self.beams.remove(beam)

    def add_enemy(self):
        if pygame.time.get_ticks() - self.enemy_add_time > self.ENEMY_TIME:
            self.enemy_add_time = pygame.time.get_ticks()
            self.enemy.append(random.choice([Alan(), Bon(), Lips()]))

    def move_enemy(self):
        for one_enemy in self.enemy:
            one_enemy.move()
            if one_enemy.remove:
                self.enemy.remove(one_enemy)
            if one_enemy.rect.colliderect(self.space.rect):
                one_enemy.remove = True
                self.space.life -= 1
                if self.space.life < 1:
                    self.game_over = True
                if one_enemy.remove:
                    self.enemy.remove(one_enemy)

    def gameover(self):
        win.blit(game_over_image, (SCREEN_WIDTH // 2 - game_over_image.get_width() // 2, SCREEN_HEIGHT // 2))

    def draw_object(self):
        for b in self.beams:
            b.draw()
        self.space.draw()
        for one in self.enemy:
            one.draw()
        for one in self.sparkles:
            one.draw()
            if one.remove:
                self.sparkles.remove(one)
    def draw_info(self):
        pygame.draw.rect(win, 'black', (0, 0, SCREEN_WIDTH, 40))
        font = pygame.font.SysFont('D2Coding', 30)
        score_text = font.render(f'SCORE: {self.score:06d}', True, 'WHITE')
        win.blit(score_text, (10, 5))
        self.space.draw_life()




game = Game()

# 게임 루프
while game.running:
    game.key_input()
    draw_bg()
    if not game.game_over:
        game.check_beam()
        game.add_enemy()
        game.move_enemy()
        game.draw_object()
    else:
        game.gameover()
    game.draw_info()
    pygame.display.update()
    clock.tick(60)

    # 화면 표시


pygame.quit()  # 파이게임 종료
