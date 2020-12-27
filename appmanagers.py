from typing import Union

import pygame as pg
from pygame import Surface
from pygame.surface import SurfaceType


class MainWindow:

    def __init__(self):
        super(MainWindow, self).__init__()
        
        # Load image icon app
        self.icon = pg.image.load('./images/icon.png')

        # Settings window
        self.window_width = 840
        self.window_height = 840
        self.pixel = 10
        self.background_color = (20, 20, 20)

        # Create window
        self.window = pg.display.set_mode((self.window_width, self.window_height))
        pg.display.set_caption('Snake')
        pg.display.set_icon(self.icon)




class ManagerScore:
    # Initial number of the account
    score = [0]

    def __init__(self):
        super(ManagerScore, self).__init__()
        
        # Load max score
        with open('./recordscore.txt') as file:
            self.global_record = int(file.read())

        # Record in the current session
        self.session_record = 0

    def save_record(self):
        if self.score[0] > self.global_record:
            with open('./recordscore.txt', 'w') as file:
                file.write(str(self.score[0]))

    def reset_record(self):
        with open('./recordscore.txt', 'w') as file:
            file.write('0')

    def to_raise(self, number: int = 1):
        self.score[0] += number

    

