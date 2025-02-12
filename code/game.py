#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame as pg
import pygame.display

from code.Const import WINDOW_WIDTH, WINDOW_HEIGHT
from code.menu import Menu


class Game:
    def __init__(self):
        pg.init()
        self.window = pg.display.set_mode(size=(WINDOW_WIDTH, WINDOW_HEIGHT))

    def run(self, ):
        while True:
            menu = Menu(self.window)
            menu.run()
            pass


