import pygame

pygame.init()

WIN_WIDTH = 500
WIN_HEIGHT = 300
WIN_SIZE = (WIN_WIDTH, WIN_HEIGHT)
win = pygame.display.set_mode(WIN_SIZE)
pygame.display.set_caption('SPRITE')
clock = pygame.time.Clock()

# 스프라이트 리스트 생성 함수
def make_sprite(sheet_image, num):
    images = []
    sprite_image_width = sheet_image.get_width() // num
    sprite_image_height = sheet_image.get_height()
    for i in range(num):
        frame = sheet_image.subsurface(pygame.Rect(sprite_image_width * i, 0, sprite_image_width, sprite_image_height))
        images.append(frame)
    return images


shinobi_run = pygame.image.load('Shinobi/Run.png')
shinobi_num = 8
shinobi_images = make_sprite(shinobi_run, shinobi_num)
shinobi_frame = 0

samurai_run = pygame.image.load('Samurai/Run.png')
samurai_num = 8
samurai_images = make_sprite(samurai_run, samurai_num)
samurai_frame = 0



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    win.fill('BLACK')
    win.blit(shinobi_images[shinobi_frame % shinobi_num], (200, 100))
    shinobi_frame += 1
    win.blit(samurai_images[samurai_frame % samurai_num], (120, 100))
    samurai_frame += 1
    pygame.display.update()
    clock.tick(20)

pygame.quit()