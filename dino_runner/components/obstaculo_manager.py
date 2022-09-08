from cProfile import label
from ctypes.wintypes import SMALL_RECT
import re
import pygame

from dino_runner.components.cactus import Cactus
from dino_runner.components.bird import Bird
from dino_runner.utils.constants import SMALL_CACTUS
from dino_runner.utils.constants import BIRD
import random

class ObstacleManager:
    def __init__ (self):
        self.obstacles = []
        self.obs = [lambda : Cactus(SMALL_CACTUS), lambda : Bird(BIRD)]

    def get_obstacle(self):
        index = random.randint(0,1)
        return self.obs[index]()
        
    def update(self, game):
        if len(self.obstacles) == 0:
            self.obstacles.append(self.get_obstacle())

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if (game.player.dino_rect.colliderect(obstacle.rect)):
                pygame.time.delay(500)
                # game.playing = False

                    
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
        
