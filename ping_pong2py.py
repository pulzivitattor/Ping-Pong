from pygame import *
back = (200, 255, 255)
win_widtn = 700
win_height = 500
window = display.set_mode((win_widtn, win_height))
display.set_caption('Ping-Pong')
window.fill(back)

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x , size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_L(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if key_pressed[K_s] and self.rect.y < win_widtn - 80:
            self.rect.y += self.speed

    def update_R(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if key_pressed[K_DOWN] and self.rect.y < win_widtn - 80:
            self.rect.y += self.speed
    
racket1 = Player('Rocket.png', 0, 200, 50, 150, 4)
racket2 = Player('Rocket2.png', 650, 200, 50, 150, 4)
ball = GameSprite('ball.png', 320, 200, 50, 50, 4)

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
        racket1.update_L()
        racket2.update_R()

        racket1.reset()
        racket2.reset()
        ball.reset()
    display.update()
    clock.tick(FPS)