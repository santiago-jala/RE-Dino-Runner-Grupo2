import pygame
from dino_runner.components.Obstaculo import Obstacle
import random

class Cactus(Obstacle):
    def __init__ (self, image):
        self.type = random.randint(0, 2)
        super(). __init__ (image, self.type)
        self.rect.y = 320 #220