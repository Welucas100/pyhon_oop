import pygame

pygame.init()

WIN_WIDTH = 400
WIN_HEIGHT = 600
WIN_SIZE = (WIN_WIDTH, WIN_HEIGHT)
win = pygame.display.set_mode(WIN_SIZE)
pygame.display.set_caption('SPACE')
clock = pygame.time.Clock()


def make_sprite(sheet_name, num):
    images = []
    sprite_width = sheet_name.get_width() // num
    sprite_height = sheet_name.get_height()
    for i in range(num):
        sprite = sheet_name.subsurface(pygame.Rect(sprite_width * i, 0, sprite_width, sprite_height))
        sprite = pygame.transform.scale(sprite, (sprite_width * 2, sprite_height * 2))
        images.append(sprite)
    return images


# player Class
class Player:
    LEFT = 0
    CENTER = 1
    RIGHT = 2

    def __init__(self):
        self.image = ship_images[Player.CENTER]
        self.speed = 5
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.x = WIN_WIDTH // 2
        self.y = WIN_HEIGHT - self.height * 2
        self.booster_frame = 0
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def turn_left(self):
        if self.x > 0:
            self.x -= self.speed
            self.image = ship_images[Player.LEFT]

    def turn_right(self):
        if self.x < WIN_WIDTH - self.width:
            self.x += self.speed
            self.image = ship_images[Player.RIGHT]

    def draw(self):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        win.blit(self.image, (self.x, self.y))
        win.blit(booster_images[self.booster_frame % 2], (self.x, self.y+self.height))
        self.booster_frame += 1

ship_sheet = pygame.image.load('MiniPixel3/Player ship/Player_ship (16 x 16).png')
ship_num = 3
ship_images = make_sprite(ship_sheet, ship_num)
booster_sheet = pygame.image.load('MiniPixel3/Player ship/Boosters (16 x 16).png')
booster_num = 2
booster_images = make_sprite(booster_sheet, booster_num)



player = Player()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYUP:
            player.image = ship_images[Player.CENTER]

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]:
        player.turn_left()
    if pressed[pygame.K_RIGHT]:
        player.turn_right()
    win.fill('BLACK')
    player.draw()
    pygame.display.update()
    clock.tick(30)


pygame.quit()