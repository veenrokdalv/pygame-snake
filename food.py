from random import randrange, choice
import pygame as pg
import appmanagers as am


class Food(am.MainWindow):

    def __init__(self):
        super(Food, self).__init__()

        self.block_surface = pg.Surface((self.pixel, self.pixel))
        self.block_position = self.block_surface.get_rect(topleft=(
            randrange(0, pg.display.get_window_size()[0] - self.pixel, self.pixel),
            randrange(0, pg.display.get_window_size()[1] - self.pixel, self.pixel)))
        self.block_surface.fill((255, 38, 0))

    def blit(self):
        self.window.blit(self.block_surface, self.block_position)
