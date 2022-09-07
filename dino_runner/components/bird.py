from math import gamma
import pygame
from dino_runner.components.Obstaculo import Obstacle

from dino_runner.utils.constants import BIRD
import random

class Bird(Obstacle):
    def __init__ (self, image):
        self.type = 0
        super(). __init__ (image, self.type)
        bird_posible_spawns = [320, 280, 220]
        self.rect.y = bird_posible_spawns[random.randint(0, 2)] 
    

