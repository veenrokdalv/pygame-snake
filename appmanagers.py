from typing import Union

import pygame as pg
from pygame import Surface
from pygame.surface import SurfaceType


class MainWindow:

    window: Union[Surface, SurfaceType]

    def __init__(self, width: int = 640, height: int = 640, pixel: int = 10):
        super(MainWindow, self).__init__()
        
        # Load image icon app
        self.icon = pg.image.load('./images/icon.png')

        # Settings window
        self.pixel = pixel
        self.background_color = (20, 20, 20)

        # Create window
        self.window = pg.display.set_mode((width, height))
        pg.display.set_caption('Snake')
        pg.display.set_icon(self.icon)


class ManagerScore:

    def __init__(self):
        super(ManagerScore, self).__init__()
        
        # Load max score
        with open('./recordscore.txt') as file:
            self.global_record = int(file.read())

        # Initial number of the account
        self.score = 0

        # Record in the current session
        self.session_record = 0

    def save_record(self):
        if self.score > self.global_record:
            with open('./recordscore.txt', 'w') as file:
                file.write(str(self.score))

    def reset_record(self):
        with open('./recordscore.txt', 'w') as file:
            file.write('0')

    def to_raise(self, number: int = 1):
        self.score += number
