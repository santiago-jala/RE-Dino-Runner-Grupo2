import pygame
from dino_runner.components.Clouds.Background import Background

from dino_runner.components.Clouds.Cloud import Cloud
from dino_runner.utils.constants import CLOUD
import random

class BackgroundManager:
    def __init__ (self):
        self.background = []
        #self.cloud = Cloud(CLOUD)

    def update(self, game):
        if len(self.background) == 0:
            self.background.append(Cloud(CLOUD))
        for back in self.background:
            back.update(game.game_speed, self.background)


    def draw(self, screen):
        for back in self.background:
            back.draw(screen)
