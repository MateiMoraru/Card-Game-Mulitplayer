import random
import pygame
from spritesheet import *
from rect import *
from window import Window
from text import *

class Environment:
    def __init__(self, window: Window, spritesheet: Spritesheet, font: pygame.Font):
        self.window = window
        self.spritesheet = spritesheet 
        self.font = font
        self.sprite_size = 6


    def draw(self):
        pass

    def loop(self):
        dt = self.window.delta_time

        pass