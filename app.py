import sys
import pygame as pg


class App:

    def __init__(self, width: int = 640, height: int = 640, pixel: int = 10):
        """
            Initialization main settings app.
            :param width: Width window.
            :param height: Height window.
            :param pixel: size virtual pixel window.
            """
        # Load image icon app
        self.icon = pg.image.load('./images/Icon.png')

        # Load max score
        with open('./maxscore.txt') as file:
            self.max_score = int(file.read())

        # Settings window
        self.background_color = (20, 20, 20)

        # WARMING! : Game speed depends on fps
        self.framerate = pg.time.Clock().tick
        self.fps = 5

        # Create window
        self.window = pg.display.set_mode((width, height))
        pg.display.set_caption('Snake')
        pg.display.set_icon(self.icon)

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

        # Game management
        if events_keyboard[pg.K_UP]:
            print('Изменено направление змейки K_UP')
        if events_keyboard[pg.K_DOWN]:
            print('Изменено направление змейки K_DOWN')
        if events_keyboard[pg.K_LEFT]:
            print('Изменено направление змейки K_LEFT')
        if events_keyboard[pg.K_RIGHT]:
            print('Изменено направление змейки  K_RIGHT')



    def move_objects(self):
        """
        Process which sets the provision of objects at a window
        :return: None
        """
        pass

    def blit_objects(self):
        """
        Process of display of all objects in a window
        :return: None
        """
        pass

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

