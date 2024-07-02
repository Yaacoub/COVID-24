import os
import pygame
from Source.Views.Welcome import Welcome


if __name__ == "__main__":

    root = os.path.dirname(os.path.realpath(__file__))
    music = os.path.join(root, "Assets", "Audio", "COVID-24.mp3")

    pygame.mixer.init()
    pygame.mixer.music.load(music)
    pygame.mixer.music.play(loops=-1)
    pygame.mixer.music.set_volume(0.5)

    app = Welcome()
    app.mainloop()
