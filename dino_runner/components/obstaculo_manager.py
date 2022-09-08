from ctypes.wintypes import SMALL_RECT
import pygame

from dino_runner.components.cactus import Cactus
from dino_runner.components.bird import Bird
from dino_runner.utils.constants import SMALL_CACTUS
from dino_runner.utils.constants import BIRD
import random

class ObstacleManager:
    def __init__ (self):
        self.obstacles = []

    def get_obstacle(self, ):
        index = random.randint(0,1)
        if index == 0:
            return Cactus(SMALL_CACTUS)
        elif index == 1:
            return Bird(BIRD)
        

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
        
