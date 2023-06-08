from pygame import *
from random import randint
init()

win_width = 1280
win_height = 720


class GameSprite(sprite.Sprite):
    def  __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(size_x,size_y))
        self.speed = player_speed 
        self.rect = self.image.get_rect()
        self.rect.x=player_x
        self.rect.y=player_y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))
class Player(GameSprite):
    def update_l_r(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x >5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width -80:
            self.rect.x += self.speed
    def update_a_d(self):
        if keys[K_UP] and self.rect.y >5 :
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y <win_height -80:
            self.rect.y +=self.speed

class Enemy(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed, side='left'):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y, player_speed)        
        self.side = side
        

    def update(self):
        global side
        if self.side == 'right'
            self.rect.x -= self.speed
        if self.side == 'left'
            self.rect.x += self.speed
window = display.set_mode((win_width, win_height))
display.set_caption('Arcada')
background = transform.scale(image.load('images/bgr.png'),(win_width, win_height))

game = True
finish = False
clock = time.Clock()
FPS = 60

#mixer.init()

while game:
    for e in event.get():
        if e.type == QUIT:
            game=False
    

    display.update()
    clock.tick(FPS)