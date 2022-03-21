from pygame import *

window = display.set_mode((700, 500))
display.set_caption('Пинг-понг')
background = transform.scale(image.load('galaxy.jpg'), (700, 500))
class Gamesprite(sprite.Sprite):
    def __init__(self, player_image, ratio, player_x, player_y, speedx, speedy):
        super().__init__()
        self.image = transform.scale(image.load(player_image), ratio)
        self.speedx = speedx
        self.speedy = speedy
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    def move2(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speedy
        if keys[K_DOWN] and self.rect.y < 450:
            self.rect.y += self.speedy
        self.reset()
    def move1(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speedy
        if keys[K_s] and self.rect.y < 450:
            self.rect.y += self.speedy
        self.reset()
    def bounce(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
            self.speedx *= -1
        if self.rect.y < 5 or self.rect.y > 450:
            self.speedy *= -1
        self.reset()
player1 = Gamesprite('racket.png', (65, 130), 40, 200, 0, 4)
player2 = Gamesprite('racket.png', (65, 130), 600, 200, 0, 4)
ball = Gamesprite('ball.png', (50, 50), 320, 200, 4, 4)     
game = True
clock = time.Clock()
FPS = 60
while game:
    clock.tick(FPS)
    window.blit(background, (0, 0))
    player1.move1()
    player2.move2()
    ball.bounce()
    for e in event.get():
        if e.type == QUIT:
            quit()
            exit(0)
    display.update()
