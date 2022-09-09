import pygame

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
            print("Cloud clas")

    def draw(self, screen):
        for back in self.background:
            back.draw(screen)
            print("Cloud drawed")