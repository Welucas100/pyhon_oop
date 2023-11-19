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





# 스프라이트 분할
def split_sprite(sprite_image, split_num, ss = 2):
    sprite_scale = ss
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
    LEFT = 0
    CENTER = 1
    RIGHT = 2

    def __init__(self):
        self.image = space_image
        self.idx = Space.CENTER
        self.booster_image = booster_images[self.idx]
        self.booster_image_idx = 0
        self.booster_time = pygame.time.get_ticks()
        self.size = self.image[self.idx].get_width()
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT - self.size * 2
        self.speed = 3
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)


    def move_left(self):
        self.idx = Space.LEFT
        if self.x > 0:
            self.x -= self.speed

    def move_right(self):
        self.idx = Space.RIGHT
        if self.x < SCREEN_WIDTH - self.size:
            self.x += self.speed
    def draw(self):
        self.booster_image = booster_images[self.idx]
        win.blit(self.image[self.idx], (self.x, self.y))
        win.blit(self.booster_image[self.booster_image_idx], (self.x, self.y + self.size))
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)
        if pygame.time.get_ticks() - self.booster_time > 50:
            self.booster_time = pygame.time.get_ticks()
            self.booster_image_idx += 1
            if self.booster_image_idx >= booster_image_num:
                self.booster_image_idx = 0
# Beam Class
class Beam:
    def __init__(self):
        self.x = space.x
        self.y = space.y
        self.speed = 5
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
        self.size = 32
        self.x = random.randint(0, SCREEN_WIDTH - self.size)
        self.y = random.randint(-self.size * 3, - self.size)
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


# Bon(Enemy) Class
class Bon(Enemy):
    def __init__(self):
        self.sx = 1
        super().__init__(bon_image, bon_image_num, 1, 80)

    def move(self):
        self.x += self.sx
        if self.x > SCREEN_WIDTH or self.x < 0:
            self.sx *= -1
        super().move()

# Lips(Enemy) Class
class Lips(Enemy):
    def __init__(self):
        super().__init__(lips_image, lips_image_num, 4, 50)
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


# 게임 초기화

space = Space()  # 우주선 객체 생성
sparkles = []
beams = []#미사일 초기화

# 적 리스트 생성
enemy = [Alan()]
enemy_add_time = pygame.time.get_ticks()
ENEMY_TIME = 1000

# 플레이어 생성
# 미사일 리스트 생성

# 게임 루프
running = True
while running:
    # 키 입력 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYUP:
            space.idx = Space.CENTER
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                beams.append(Beam())

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]:
        space.move_left()
    if pressed[pygame.K_RIGHT]:
        space.move_right()
    #if pressed[pygame.K_SPACE]:
     #   beams.append(Beam())


    # 미사일 이동

    for one in beams:
        one.move()
        # 충돌 처리
        for x in enemy:
            if one.rect.colliderect(x.rect):
                sparkles.append(Sparkle(x.x, x.y))
                one.remove = True
                x.remove = True
        if one.remove:
            beams.remove(one)
    # 적추가
    if pygame.time.get_ticks() - enemy_add_time > ENEMY_TIME:
        enemy_add_time = pygame.time.get_ticks()
        enemy.append(random.choice([Alan(), Bon(), Lips()]))

    # 적 이동
    for one in enemy:
        one.move()
        if one.remove:
            enemy.remove(one)
    # 화면 표시
    win.fill('black')
    draw_bg()
    for b in beams:
        b.draw()
    space.draw()
    for one in enemy:
        one.draw()
    for one in sparkles:
        one.draw()
        if one.remove:
            sparkles.remove(one)
    pygame.display.update()
    clock.tick(60)

pygame.quit()  # 파이게임 종료
