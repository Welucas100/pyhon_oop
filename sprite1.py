# sprite1.py

import pygame

pygame.init()

WIN_WIDTH = 500
WIN_HEIGHT = 500
WIN_SIZE = (WIN_WIDTH, WIN_HEIGHT)
win = pygame.display.set_mode(WIN_SIZE)
pygame.display.set_caption("SPRITE SHEET")
clock = pygame.time.Clock()

# 스프라이트 시트 불러오기
shinobi_walk_sheet = pygame.image.load("Shinobi/Walk.png")
samurai_walk_sheet = pygame.image.load("Samurai/Walk.png")

# 이미지 추출
shinobi_sprite_num = 8
shinobi_sprite_width = shinobi_walk_sheet.get_width() // shinobi_sprite_num
shinobi_sprite_height = shinobi_walk_sheet.get_height()
shinobi_images = []

samurai_sprite_num = 8
samurai_sprite_width = samurai_walk_sheet.get_width() // samurai_sprite_num
samurai_sprite_height = samurai_walk_sheet.get_height()
samurai_image = []

for idx in range(shinobi_sprite_num):
    frame = shinobi_walk_sheet.subsurface(pygame.Rect(shinobi_sprite_width * idx, 0, shinobi_sprite_width, shinobi_sprite_height))
    shinobi_images.append(frame)

# 이미지의 프레임 번호
shinobi_frame_num = 0

for idx in range(samurai_sprite_num):
    frame = samurai_walk_sheet.subsurface(pygame.Rect(samurai_sprite_width * idx, 0, samurai_sprite_width, samurai_sprite_height))
    samurai_image.append(frame)

samurai_frame_num = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    win.fill("BLACK")
    win.blit(shinobi_images[shinobi_frame_num], (200, 100))
    shinobi_frame_num += 1
    if shinobi_frame_num > 7:
        shinobi_frame_num = 0
    win.blit(samurai_image[samurai_frame_num], (150, 100))
    samurai_frame_num += 1
    if samurai_frame_num > 7:
        samurai_frame_num = 0
    pygame.display.update()
    clock.tick(10)

pygame.quit()