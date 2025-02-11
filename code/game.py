#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame as pg
import pygame.display

from code.menu import Menu


class Game:
    def __init__(self):
        pg.init()
        self.window = pg.display.set_mode(size=(600, 480))

    def run(self, ):
        while True:
            menu = Menu(self.window)
            menu.run()


            # Check for all events
            # for event in pygame.event.get():
            #     if event.type == pygame.QUIT:
            #
            #         pygame.quit()  # Close Window
            #         quit()  # end pygame