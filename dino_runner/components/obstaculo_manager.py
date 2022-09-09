from cProfile import label
from ctypes.wintypes import SMALL_RECT
import re
from sre_parse import State
from turtle import title
import pygame
from dino_runner.components.cactus2 import Cactus2
from dino_runner.components.cactus import Cactus
from dino_runner.components.bird import Bird
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, GAME_OVER, BIRD
from dino_runner.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH
from dino_runner.components.TITLES import Titles

import random

class ObstacleManager:
    def __init__ (self):
        self.obstacles = []
        self.obs = [lambda : Cactus(SMALL_CACTUS), lambda : Bird(BIRD), lambda : Cactus2(LARGE_CACTUS)]
        self.state = False
        title = Titles

    def get_obstacle(self):
        index = random.randint(0,2)
        return self.obs[index]()
    def update(self, game):
        if len(self.obstacles) == 0:
            self.obstacles.append(self.get_obstacle())

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                if not game.player.shield:
                    if not game.player.has_lives:
                        game.player_heart_manager.reduce_heart_count()
                        if game.player_heart_manager.heart_count > 0:
                            game.player.has_lives = True
                            self.obstacles.pop()
                            start_transition_time = pygame.time.get_ticks()
                            game.player.lives_transition_time = start_transition_time + 1000
                        else:
                            self.state = True
                            self.draw_title
                            pygame.time.delay(500)
                            game.playing = False
                            game.death_count += 1
                            break
                        
    def draw(self, screen):
        if self.state:
            Titles(GAME_OVER).draw(screen)
        for obstacle in self.obstacles:
            obstacle.draw(screen)
        
    def draw_title(self, screen):
        Titles(GAME_OVER).draw(screen)
