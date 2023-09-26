from pygame import *
win_width = 700
win_height = 500
display.set_caption("Shooter")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load('fon.jpeg'), (win_width, win_height))
run = True 

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    window.blit(background,(0,0))
    display.update()
    time.delay(50)


