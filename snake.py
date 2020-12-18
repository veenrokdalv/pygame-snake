import pygame as pg


class Snake:

    def __init__(self, window: object, pixel: int):
        """
        Designer of a class.
        :param window: Surface, on which the snake will appear.
        :param pixel: Size virtual pixel.
        """
        self.window = window
        self.pixel = pixel

        self.position = [pg.display.get_window_size()[0] // 2, pg.display.get_window_size()[1] // 2]

        self.surface_block = pg.Surface((self.pixel, self.pixel))
        self.block_position = self.surface_block.get_rect()

        self.surface_block.fill((0, 249, 0))

    def blit(self):
        self.window.blit(self.surface_block, self.position)
