import sys
import pygame as pg
import appmanagers as am
from food import Food
from snake import Snake


class App(am.ManagerScore, am.MainWindow):

    def __init__(self):
        """
            Initialization main settings app.
            :param width: Width window.
            :param height: Height window.
            :param pixel: size virtual pixel window.
            """
        super().__init__()

        # WARMING! : Game speed depends on fps
        self.framerate = pg.time.Clock().tick
        self.fps = 5

        # Example Snake
        self.snake = Snake()

        # Example Food
        self.food = Food(self.snake.block_position)

    def close(self):
        """
        Finishes all processes of the appendix
        :return: None
        """
        self.save_record()
        pg.quit()
        sys.exit()

    def event_handler(self):
        """
        Catches all events of the appendix
        :return:
        """
        # Events from the keyboard
        events_keyboard = pg.key.get_pressed()

        # Events which close the appendix
        [self.close() for event in pg.event.get() if event.type == pg.QUIT]
        if events_keyboard[pg.K_ESCAPE]:
            self.close()

        self.snake.event_key(events_keyboard)

    def move_objects(self):
        """
        Process which sets the provision of objects at a window
        :return: None
        """
        self.snake.movement()
        self.food.move()

    def blit_objects(self):
        """
        Process of display of all objects in a window
        :return: None
        """
        self.window.fill(self.background_color)

        self.food.blit()
        self.snake.blit()

        pg.display.update()

    def start(self):
        """
        Start of all processes of the appendix
        :return: None
        """
        while True:
            self.event_handler()
            self.move_objects()
            self.blit_objects()
            self.framerate(self.fps)