from math import gamma
import pygame
from dino_runner.components.Obstaculo import Obstacle


import random

class Bird(Obstacle):
    def __init__ (self, image):
        self.type = 0
        super(). __init__ (image, self.type)
        bird_posible_spawns = [330, 272, 240]
        self.rect.y = bird_posible_spawns[random.randint(0, 2)] 
        self.animation = 0

    def draw(self, screen):
        screen.blit(self.image[self.type], self.rect)
        self.animation += 1
        if self.animation % 7 == 0:
            self.type = (self.type + 1) % 2



