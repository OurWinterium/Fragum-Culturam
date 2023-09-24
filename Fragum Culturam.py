from pygame import *
from random import *

#init()
mixer.init()

window = display.set_mode((384, 384))
display.set_caption("Fragum Culturam")
background = transform.scale(image.load("image.png"), (384, 384))

mixer.music.load('Beyond the Lows - The Whole Other.mp3')
mixer.music.play(-1)

game = True

while game:
    window.blit(background, (0, 0))
    for e in event.get():
        if e.type == QUIT:
            game = False