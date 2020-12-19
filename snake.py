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

        # Settings snake
        self.length = 1
        self.body = []
        self.direction = 'up'
        self.surface_block = pg.Surface((self.pixel, self.pixel))

        # Start position
        self.block_position = self.surface_block.get_rect(topleft=(pg.display.get_window_size()[0] // 2, pg.display.get_window_size()[1] // 2))

        self.surface_block.fill((0, 249, 0))

    def blit(self):
        self.control_length()
        for block in self.body:
            self.window.blit(self.surface_block, block)

    def control_length(self):
        self.body.append(self.block_position[:])

        if self.length < len(self.body):
            self.body.pop(0)

    def event_key(self, events_keyboard):

        if events_keyboard[pg.K_UP] and self.direction != 'down':
            self.direction = 'up'
        if events_keyboard[pg.K_DOWN] and self.direction != 'up':
            self.direction = 'down'
        if events_keyboard[pg.K_LEFT] and self.direction != 'right':
            self.direction = 'left'
        if events_keyboard[pg.K_RIGHT] and self.direction != 'left':
            self.direction = 'right'

    def movement(self):
        """
        Changes the direction of a snake, dependence on the pressed key.
        :return: None
        """
        if self.direction == 'up':
            self.block_position.y -= self.pixel
        if self.direction == 'down':
            self.block_position.y += self.pixel
        if self.direction == 'left':
            self.block_position.x -= self.pixel
        if self.direction == 'right':
            self.block_position.x += self.pixel

        self.check_collision_wall()

    def check_collision_wall(self):
        """
        Check on collision with a wall.
        :return: None
        """
        if self.block_position.left < 0:
            self.block_position.right = pg.display.get_window_size()[0]
        elif self.block_position.right > pg.display.get_window_size()[0]:
            self.block_position.left = 0
        if self.block_position.top < 0:
            self.block_position.bottom = pg.display.get_window_size()[1]
        elif self.block_position.bottom > pg.display.get_window_size()[1]:
            self.block_position.top = 0
