from pygame import *
from random import *
#from pygame.locals import *
init()
mixer.init()

window = display.set_mode((700, 700))
display.set_caption("Fragum Culturam")
background = transform.scale(image.load("fon.jpg"), (700, 700))

'''
background = transform.scale(image.load("image.png"), (700, 700))
'''

mixer.music.load('Sound_2.mp3')
mixer.music.play(-1)

lost = 0

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
        #for e in events.get():
        if event.key == pygame.MOUSEBUTTONUP:
            lost += 1
                #if self.rect.collidepoint(event.pos):
                    #self.callback()

fontTxt = font.SysFont('Arial', 30)

Fragares = sprite.Group()
for i in range(4):
    Fragaria = Sprite('Fragaria.png', randint(30, 670), randint(379, 600), 0)
    Fragares.add(Fragaria)

clock = time.Clock()
FPS = 60

game = True

while game:
    window.blit(background, (0, 0))
    for e in event.get():
        if e.type == QUIT:
            game = False

    window.blit(fontTxt.render('Собрано: '+str(lost), True, (255,255,255)), (240, 100))
    Fragares.update()
    Fragares.draw(window)
    clock.tick(FPS)
    display.update()