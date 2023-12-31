from pygame import *
win_width = 700
win_height = 500
display.set_caption("Shooter")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load('fon.jpeg'), (win_width, win_height))
run = True 
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
  
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 100:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 100:
            self.rect.y += self.speed
ball=GameSprite('pin.png',250,250,100,80,10)
player1=Player('platform.png', 4,100,40,100,10)
player2=Player('platform.png', 660,100,40,100,10)

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    window.blit(background,(0,0))
    ball.reset()
    player1.update_l()
    player1.reset()
    player2.update_r()
    player2.reset()
    display.update()
    time.delay(50)


