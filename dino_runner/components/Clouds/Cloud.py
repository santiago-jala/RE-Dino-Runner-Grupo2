from math import gamma
import pygame
from dino_runner.components.Clouds.Background import Background
import random

class Cloud(Background):
    def __init__ (self, image):
        super(). __init__ (image) 
        self.rect.y = random.randint(20, 200)


