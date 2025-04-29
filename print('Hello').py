from pygame import *
back = (200, 255, 255)
win_widtn = 700
win_height = 500
window = display.set_mode((win_widtn, win_height))
display.set_caption('Ping-Pong')
window.fill(back)

game = True
finish = False
clock = time.Clock()
FPS = 60
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
            window.fill(back)
    display.update()
    clock.tick(FPS)