
from pygame import *

window = display.set_mode((700, 500))
display.set_caption('Пинг-понг')
background = transform.scale(image.load('galaxy.jpg'), (700, 500))
class Gamesprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    def move1(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 395:
            self.rect.y += self.speed
        self.reset()
    def move2(self):
        keys = key.get_pressed()
        if keys[K_W] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_S] and self.rect.y < 395:
            self.rect.y += self.speed
        self.reset()
player1 = Gamesprite('racket.png', 275, 400, 4)
player2 = Gamesprite('racket.png', 275, 400, 4)     
game = True
while game:
    window.blit(background, (0, 0))
    player1.move1()
    player2.move2()
    for e in event.get():
        if e.type == QUIT:
            quit()
            exit(0)
    display.update()
