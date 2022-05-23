from pygame import *
font.init()
font1 = font.SysFont('Arial', 50)
font = font.SysFont('Arial', 100)
hj = 15
dg = 1
class Player(sprite.Sprite):
    def __init__(self, c1, c2, c3, x, y, width, height, speed):
        super().__init__()
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3
        self.width = width
        self.height = height
        self.image = Surface((self.width, self.height))
        self.image.fill((self.c1, self.c2, self.c3))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    def update2(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < win_height - 155:
            self.rect.y += self.speed  
    def update1(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < win_height - 155:
            self.rect.y += self.speed  
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Bll(sprite.Sprite):
    def __init__(self, c1, c2, c3, x, y, width, height, speed_x, speed_y):
        super().__init__()
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3
        self.width = width
        self.height = height
        self.image = Surface((self.width, self.height))
        self.image.fill((self.c1, self.c2, self.c3))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed_x = speed_x
        self.speed_y = speed_y
    def update(self):
        global finish
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.y > win_height - 50 or self.rect.y < 0:
            ball._y()
        if self.rect.x < 0 or self.rect.x > win_width - 50:
            finish = False
            window.blit(lose1, (win_width / 2 - 250, win_height / 2 - 75))
    def _x(self):
        self.speed_x *= -1
    def _y(self):
        self.speed_y *= -1
    def y(self):
        self.speed_y *= 1
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
win_width = 1000
win_height = 700
window = display.set_mode((win_width, win_height))
display.set_caption('PING-PONG')
player1 = Player(255, 255, 255, 50, win_height/ 2 - 150, 50, 150, 4) 
player2 = Player(255, 255, 255, win_width - 100, win_height/ 2 - 150, 50, 150, 4)
ball = Bll(255, 255, 255, win_width / 2 - 50, win_height / 2 - 50, 50, 50, 3, 3)
lose1 = font.render('YOU LOSE!', True, (255, 255, 255))
score = 0
game = True
finish = True
run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            game = False
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                run = False
        window.fill((0, 0, 0))
        p = font.render('PING-PONG', True, (255, 255, 255))
        we = font1.render('PRESS "SPACE" TO START', True, (255, 255, 255))
        window.blit(p, (win_width / 2 - 235, win_height / 2 - 135))
        window.blit(we, (win_width / 2 - 265, win_height / 2 + 70))
        display.update()
        time.delay(15)
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish:
        if score == dg * 10:
            hj += 15
            dg *= 10
        window.fill((0, 0, 0))
        lose2 = font1.render(str(score), True, (255, 255, 255))
        player1.update1()
        player2.update2()
        ball.update()
        window.blit(lose2, (win_width / 2 - hj, 5))
        if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
            ball._x()
            ball.y()
            score = score + 1
        player1.reset()
        player2.reset()    
        ball.reset()
    display.update()
    time.delay(15)