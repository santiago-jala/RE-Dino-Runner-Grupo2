from math import gamma
import pygame
from dino_runner.components.Clouds.Background import Background
import random

class Cloud(Background):
    def __init__ (self, image):
        super(). __init__ (image)
        cloud_posible_spawns = [370, 370, 300]
        self.rect.y = cloud_posible_spawns[random.randint(0, 2)] 
        


