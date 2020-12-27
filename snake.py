import pygame as pg
import appmanagers as am



class Snake(am.MainWindow, am.ManagerScore):

    def __init__(self):
        """
        Designer of a class.
        :param window: Surface, on which the snake will appear.
        :param pixel: Size virtual pixel.
        """
        super().__init__()

        # Settings snake
        self.body = []
        self.direction = 'up'
        self.surface_block = pg.Surface((self.pixel, self.pixel))

        # Start position
        self.block_position = self.surface_block.get_rect(topleft=(pg.display.get_window_size()[0] // 2, pg.display.get_window_size()[1] // 2))

        self.surface_block.fill((0, 249, 0))

    def blit(self):
        self.control_length()
        self.check_collision_tail()
        for block in self.body:
            self.window.blit(self.surface_block, block)

    def control_length(self):
        self.body.append(self.block_position[:])

        if self.score[0] + 1 < len(self.body):
            self.body.pop(0)
    
    def reset_position(self):
        self.block_position.x = self.window_width//2
        self.block_position.y = self.window_height//2
    
    def check_collision_tail(self):
        for block in self.body[:-1]:
            if self.block_position.colliderect(block):
                self.save_record()
                self.body = []
                self.score[0] = 0
                self.reset_position()


    def event_key(self, events_keyboard):

        if events_keyboard[pg.K_UP] and self.direction != 'down':
            self.direction = 'up'
        elif events_keyboard[pg.K_DOWN] and self.direction != 'up':
            self.direction = 'down'
        elif events_keyboard[pg.K_LEFT] and self.direction != 'right':
            self.direction = 'left'
        elif events_keyboard[pg.K_RIGHT] and self.direction != 'left':
            self.direction = 'right'

    def movement(self):
        """
        Changes the direction of a snake, dependence on the pressed key.
        :return: None
        """
        if self.direction == 'up':
            self.block_position.y -= self.pixel
        elif self.direction == 'down':
            self.block_position.y += self.pixel
        elif self.direction == 'left':
            self.block_position.x -= self.pixel
        elif self.direction == 'right':
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
