from pygame import *

window = display.set_mode((700, 500))
display.set_caption('догонялки')

bg = transform.scale(image.load('Вагонетка.png'), (700, 500))


mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()

money = mixer.Sound('money.ogg')
kick = mixer.Sound('kick.ogg')

font.init()
font = font.SysFont('Arial', 70)
win = font.render('YOU WIN', True, (0, 255, 0))
lose = font.render('YOU LOSE', True, (255, 0, 0))

class Gamesprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(Gamesprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 430 :
            self.rect.y += self.speed
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 630:
            self.rect.x += self.speed
class Enemy(Gamesprite):
    direction = "left"
    def update(self):
        if self.rect.x <= 400:
            self.direction = "right"
        if self.rect.x >= 630:
            self.direction = "left"
        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed


class Wall(sprite.Sprite):
    def __init__(self, color1, color2, color3, wall_x, wall_y, wall_width, wall_hight):
        super().__init__()
        self.image = Surface((wall_width, wall_hight))
        self.image.fill((color1, color2, color3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def DrawWall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


w1 = Wall(0, 0, 128, 100, 0, 10, 400)     
w2 = Wall(0, 0, 128, 200, 100, 10, 400)
w3 = Wall(0, 0, 128, 300, 0, 10, 400)  
w4 = Wall(0, 0, 128, 400, 100, 10, 400)
w5 = Wall(0, 0, 128, 400, 100, 230, 10)
w6 = Wall(0, 0, 128, 500, 200, 230, 10)
hero = Player('pngwing.com (2).png', 5, 420, 4)
cyborg = Enemy('cyborg.png', 620, 220, 3, )
cyborg2 = Enemy('cyborg.png', 400, 340, 4, )
gold = Gamesprite('treasure.png', 580, 420, 0)

walls = [w1, w2, w3, w4, w5, w6]

game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        window.blit(bg,(0,0))
        hero.reset()
        cyborg.reset()
        cyborg2.reset()
        gold.reset()
        hero.update()
        cyborg.update()
        cyborg2.update()
        w1.DrawWall()
        w2.DrawWall()
        w3.DrawWall()
        w4.DrawWall()
        w5.DrawWall()
        w6.DrawWall()
        if sprite.collide_rect(hero, gold):
            finish = True
            money.play()
            window.blit(win, (200, 200))
        if sprite.collide_rect(hero, cyborg):
            finish = True
            kick.play()
            window.blit(lose, (200, 200))
        if sprite.collide_rect(hero, cyborg2):
            finish = True
            kick.play()
            window.blit(lose, (200, 200))
        for i in walls:
            if sprite.collide_rect(hero, i):
                finish = True
                kick.play()
                window.blit(lose, (200, 200))


    

    

    display.update()
    time.delay(10)
