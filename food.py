from random import randrange, choice
import pygame as pg
import appmanagers as am


class Food(am.MainWindow, am.ManagerScore):

    def __init__(self, block_position_snake):
        super(Food, self).__init__()

        self.block_position_snake = block_position_snake

        self.block_surface = pg.Surface((self.pixel, self.pixel))
        self.block_surface.fill((255, 38, 0))
        self.set_position()

    @property
    def is_eaten(self):
        return self.block_position.colliderect(self.block_position_snake)



    def blit(self):
        self.window.blit(self.block_surface, self.block_position)


    def set_position(self):
        self.block_position = self.block_surface.get_rect(topleft=(
            randrange(0, self.window_width - self.pixel, self.pixel),
            randrange(0, self.window_height - self.pixel, self.pixel)))

    def move(self):
        if self.is_eaten:
            self.set_position()
            self.to_raise()
