import  pygame

pygame.init() #파이게임 초기화

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
win = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption('key EVENT')

clock = pygame.time.Clock()


class Box:
    def __init__(self):
        self.x = SCREEN_WIDTH // 2  # 화면 가로 크기를 2로 나눈 몫
        self.y = SCREEN_HEIGHT // 2
        self.size = 20
        self.color = 'green'
        self.speed = 1
        self.rect = pygame.Rect(0, 0, 0, 0)


    def move_up(self):
        if 0 <= self.y:
            self.y -= 1

    def move_down(self):
        if 580 >= self.y:
            self.y +=1
    def move_left(self):
        if 0 <= self.x:
            self.x -=1
    def move_right(self):
        if 380 >= self.x:
            self.x +=1

    def draw(self):
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)
        pygame.draw.rect(win, self.color, self.rect)



box = Box()
box_red = Box()
box_red.x = 300
box_red.y = 300
box_red.color = 'red'
box_red.size = 70
box_blue = Box()
box_blue.x = 30
box_blue.y = 300
box_blue.color = 'blue'
box_blue.size = 70




running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        box.move_up()
    if keys[pygame.K_s]:
        box.move_down()
    if keys[pygame.K_a]:
        box.move_left()
    if keys[pygame.K_d]:
        box.move_right()

    if box.rect.colliderect(box_red.rect):
        if box.size < 70:
           box.size += 1
    if box.rect.colliderect(box_blue.rect):
        if box.size > 10:
            box.size -= 1

    win.fill('black')
    box_red.draw()
    box_blue.draw()
    box.draw()
    pygame.display.update()
    clock.tick(60)


pygame.quit()

