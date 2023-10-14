from pygame import *
from random import *
import pygame as pg
import sys

init()
mixer.init()

window = display.set_mode((1050, 525))
display.set_caption("Fragum Culturam")
background = transform.scale(image.load("fon.jpg"), (1050, 525))

mixer.music.load('Sound_2.mp3')
mixer.music.play(-1)

damage_svinota = mixer.Sound('damage_svinota.ogg')
ded_svinota = mixer.Sound('ded_svinota.ogg')
svinota_p = mixer.Sound('dovolnoe-hryukane-bolshim-pyatachkom.ogg')
svinota_est = mixer.Sound('chavkan-e-hryukan-e.ogg')
pomehi = mixer.Sound('zatihayuschie-pomehi.ogg')

balance = 0

class Sprite(sprite.Sprite):
    def __init__(self, sprite_image, spriteX, spriteY, sprite_speed):
        super().__init__()
        self.image = transform.scale(image.load(sprite_image), (59, 79))
        self.rect = self.image.get_rect()
        self.rect.x = spriteX
        self.rect.y = spriteY
        self.speed = sprite_speed

    def update(self):
        self.rect.y += self.speed
        self.rect.x += self.speed

class Svinota(sprite.Sprite):
    def __init__(self, sprite_image, spriteX, spriteY, sprite_speed):
        super().__init__()
        self.image = transform.scale(image.load(sprite_image), (183, 123))
        self.rect = self.image.get_rect()
        self.rect.x = spriteX
        self.rect.y = spriteY
        self.speed = sprite_speed

    def update(self):
        self.rect.y += self.speed
        self.rect.x += self.speed

    class Demon(sprite.Sprite):
    def __init__(self, sprite_image, spriteX, spriteY, sprite_speed):
        super().__init__()
        self.image = transform.scale(image.load(sprite_image), (80, 80))
        self.rect = self.image.get_rect()
        self.rect.x = spriteX
        self.rect.y = spriteY
        self.speed = sprite_speed

    def update(self):
        self.rect.y += self.speed
        self.rect.x += self.speed

fontTxt = font.SysFont('Arial', 30)

Fragares = sprite.Group()

Fragaria_1 = Sprite('Fragaria.png', randint(20, 440), randint(20, 430), 0)
Fragares.add(Fragaria_1)

Fragaria_2 = Sprite('Fragaria.png', randint(20, 440), randint(20, 430), 0)
Fragares.add(Fragaria_2)

Fragaria_3 = Sprite('Fragaria.png', randint(20, 440), randint(20, 430), 0)
Fragares.add(Fragaria_3)

Fragaria_4 = Sprite('Fragaria.png', randint(20, 440), randint(20, 430), 0)
Fragares.add(Fragaria_4)

Fragaria_5 = Sprite('Fragaria.png', randint(20, 440), randint(20, 430), 0)
Fragares.add(Fragaria_5)

Fragaria_6 = Sprite('Fragaria.png', randint(20, 440), randint(20, 430), 0)
Fragares.add(Fragaria_6)

Fragaria_7 = Sprite('Fragaria.png', randint(20, 440), randint(20, 430), 0)
Fragares.add(Fragaria_7)

Fragaria_8 = Sprite('Fragaria.png', randint(20, 440), randint(20, 430), 0)
Fragares.add(Fragaria_8)

Mobs = sprite.Group()

svinota = False

clock = time.Clock()
FPS = 60

game = True

svinota_speed_x = 15
svinota_speed_y = 15

svin_factor = 0

svinota_xp = 5

svindown = 0

aboba = 0

helldown = 0

while game:
    window.blit(background, (0, 0))
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == MOUSEBUTTONDOWN:
            x, y = e.pos
            if Fragaria_1.rect.collidepoint(x, y):
                balance += 1
                Fragaria_1.rect.x = randint(20, 440)
                Fragaria_1.rect.y = randint(20, 430)
            if Fragaria_2.rect.collidepoint(x, y):
                balance += 1
                Fragaria_2.rect.x = randint(20, 440)
                Fragaria_2.rect.y = randint(20, 430)
            if Fragaria_3.rect.collidepoint(x, y):
                balance += 1
                Fragaria_3.rect.x = randint(20, 440)
                Fragaria_3.rect.y = randint(20, 430)
            if Fragaria_4.rect.collidepoint(x, y):
                balance += 1
                Fragaria_4.rect.x = randint(20, 440)
                Fragaria_4.rect.y = randint(20, 430)
            if Fragaria_5.rect.collidepoint(x, y):
                balance += 1
                Fragaria_5.rect.x = randint(20, 440)
                Fragaria_5.rect.y = randint(20, 430)
            if Fragaria_6.rect.collidepoint(x, y):
                balance += 1
                Fragaria_6.rect.x = randint(20, 440)
                Fragaria_6.rect.y = randint(20, 430)
            if Fragaria_7.rect.collidepoint(x, y):
                balance += 1
                Fragaria_7.rect.x = randint(20, 440)
                Fragaria_7.rect.y = randint(20, 430)
            if Fragaria_8.rect.collidepoint(x, y):
                balance += 1
                Fragaria_8.rect.x = randint(20, 440)
                Fragaria_8.rect.y = randint(20, 430)         
            if svinota == True and svin_factor == 1:
                if Svinota.rect.collidepoint(x, y):
                    svinota_xp -= 1
                    damage_svinota.play()
                    damage_svinota.play()
                    if svinota_xp == 0:
                        Svinota.kill()
                        svin_factor -= 1
                        svinota == False
                        ded_svinota.play()
                        ded_svinota.play()
                        ded_svinota.play()
    
    if balance >= 25 and svinota == False and svin_factor == 0:
        Svinota = Svinota('svinota.png', randint(15, 330), randint(15, 380), 0)
        Mobs.add(Svinota)
        svinota = True
        svin_factor += 1
    
    if svinota == True and svin_factor == 1 and svinota_xp > 0:
        Svinota.rect.x += svinota_speed_x
        Svinota.rect.y += svinota_speed_y
        if sprite.collide_rect(Fragaria_1, Svinota):
            Fragaria_1.rect.x = randint(20, 440)
            Fragaria_1.rect.y = randint(20, 430)
            svinota_est.play()
        if sprite.collide_rect(Fragaria_2, Svinota):
            Fragaria_2.rect.x = randint(20, 440)
            Fragaria_2.rect.y = randint(20, 430)
        if sprite.collide_rect(Fragaria_3, Svinota):
            Fragaria_3.rect.x = randint(20, 440)
            Fragaria_3.rect.y = randint(20, 430)
            svinota_est.play()
        if sprite.collide_rect(Fragaria_4, Svinota):
            Fragaria_4.rect.x = randint(20, 440)
            Fragaria_4.rect.y = randint(20, 430)
        if sprite.collide_rect(Fragaria_5, Svinota):
            Fragaria_5.rect.x = randint(20, 440)
            Fragaria_5.rect.y = randint(20, 430)
            svinota_est.play()
        if sprite.collide_rect(Fragaria_6, Svinota):
            Fragaria_6.rect.x = randint(20, 440)
            Fragaria_6.rect.y = randint(20, 430)
        if sprite.collide_rect(Fragaria_7, Svinota):
            Fragaria_7.rect.x = randint(20, 440)
            Fragaria_7.rect.y = randint(20, 430)
            svinota_est.play()
        if sprite.collide_rect(Fragaria_8, Svinota):
            Fragaria_8.rect.x = randint(20, 440)
            Fragaria_8.rect.y = randint(20, 430)
        
        if svindown == 0:
            svinota_p.play()

        if svindown < 40:
            svindown += 1
        if svindown >= 40:
            svindown = 0
    
    '''
    if ball.rect.colliderect(player_1.rect) or ball.rect.colliderect(player_2.rect):
        ball_speed_y *= 1
        ball_speed_x *= -1
        Pong.play()
    '''

    if balance >= 25 and svinota == True:
        if Svinota.rect.x < 15:
            svinota_speed_x *= -1
        if Svinota.rect.x > 330:
            svinota_speed_x *= -1
        if Svinota.rect.y < 15:
            svinota_speed_y *= -1
        if Svinota.rect.y > 380:
            svinota_speed_y *= -1

    if balance >= 75 and aboba == 0:
        mixer.music.pause()
        aboba += 1

    if balance >= 85 and aboba == 1:
        if helldown == 0:
            pomehi.play()

        if helldown < 120:
            helldown += 1
        if helldown >= 120:
            helldown = 0

    window.blit(fontTxt.render('Баланс: '+str(balance), True, (255,255,255)), (733, 167))
    Fragares.update()
    Fragares.draw(window)
    Mobs.update()
    Mobs.draw(window)
    clock.tick(FPS)
    display.update()
display.update()