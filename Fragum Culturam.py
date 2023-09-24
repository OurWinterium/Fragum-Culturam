from pygame import *
from random import *

#init()
mixer.init()

window = display.set_mode((384, 384))
display.set_caption("Fragum Culturam")
background = transform.scale(image.load("image.png"), (384, 384))

mixer.music.load('Beyond the Lows - The Whole Other.mp3')
mixer.music.play(-1)

class Knopka(sprite.Sprite):
    def __init__(self, sprite_image, spriteX, spriteY, sprite_speed):
        super().__init__()
        self.image = transform.scale(image.load(sprite_image), (70, 30))
        self.rect = self.image.get_rect()
        self.rect.x = spriteX
        self.rect.y = spriteY
        self.speed = sprite_speed
    def update(self):
        self.rect.y += self.speed
        self.rect.x += self.speed

Knopki = sprite.Group()
Knopka_1 = Knopka('a.bmp', 100, 100, 0)
Knopki.add(Knopka_1)

clock = time.Clock()
FPS = 60

game = True

while game:
    window.blit(background, (0, 0))
    for e in event.get():
        if e.type == QUIT:
            game = False

    Knopki.update()
    Knopki.draw(window)
    clock.tick(FPS)
    display.update()