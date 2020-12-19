import sys
import pygame as pg
from snake import Snake

class App:

    def __init__(self, width: int = 640, height: int = 640, pixel: int = 10):
        """
            Initialization main settings app.
            :param width: Width window.
            :param height: Height window.
            :param pixel: size virtual pixel window.
            """
        # Load image icon app
        self.icon = pg.image.load('./images/icon.png')

        # Load max score
        with open('./maxscore.txt') as file:
            self.max_score = int(file.read())

        # Settings window
        self.pixel = 64
        self.background_color = (20, 20, 20)

        # WARMING! : Game speed depends on fps
        self.framerate = pg.time.Clock().tick
        self.fps = 2

        # Create window
        self.window = pg.display.set_mode((width, height))
        pg.display.set_caption('Snake')
        pg.display.set_icon(self.icon)

        # Example Snake
        self.snake = Snake(self.window, self.pixel)

    def close(self):
        """
        Finishes all processes of the appendix
        :return: None
        """
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

    def blit_objects(self):
        """
        Process of display of all objects in a window
        :return: None
        """
        self.window.fill(self.background_color)

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