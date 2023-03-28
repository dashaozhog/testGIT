from pygame import *
from random import uniform, choice
mixer.init()

WIN_SETTING = (1800,1000)
FPS = 60
window = display.set_mode(WIN_SETTING)
SPSIZE = (100, 300)
paddle_IMG = transform.scale(image.load("paddle.png"), SPSIZE)
vect = Vector2

beep = mixer.Sound("beep.wav")
game_over = mixer.Sound("game_over.wav")

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = player_image
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self,  player_image, player_x, player_y, player_speed, typee):
        super().__init__(player_image, player_x, player_y, player_speed)
        self.typee = typee
        self.score = 0
    def update_position(self):
        keys = key.get_pressed()
        if self.typee == "left":
            if keys[K_w] and self.rect.y>0:
                self.rect.y -= self.speed
            if keys[K_s] and self.rect.y < WIN_SETTING[1]-self.rect.height:
                self.rect.y += self.speed
        elif self.typee == "right":
            if keys[K_UP] and self.rect.y>0:
                self.rect.y -= self.speed
            if keys[K_DOWN] and self.rect.y < WIN_SETTING[1]-self.rect.height:
                self.rect.y += self.speed

        self.reset()
class Ball(sprite.Sprite):
    def __init__(self, color = (181, 16, 16), radius=50, speed = 7):
        super().__init__()
        self.color = color
        self.radius = radius
        self.rect = Rect(0,0,self.radius*2,self.radius*2)
        self.rect.x = WIN_SETTING[0]/2
        self.rect.y = WIN_SETTING[1]/2
        self.speed = speed
        self.direction = vect(choice((self.speed,-self.speed)), choice((self.speed,-self.speed)))
    def draw(self):
        draw.circle(window, self.color,(self.rect.x, self.rect.y), self.radius)
    def move(self, player1, player2):
        DOWN = WIN_SETTING[1]-self.radius
        UP = self.radius
        self.rect.move_ip(self.direction)
        if sprite.collide_rect(player1, self) or sprite.collide_rect(player2, self):
            mixer.Sound.play(beep)
            self.direction[0] *=-1.1
            self.direction[1] *=1
        if self.rect.y >= WIN_SETTING[1]-self.radius or self.rect.y <= 0:
            self.direction[1]*=-1
            self.direction[0]*=1
