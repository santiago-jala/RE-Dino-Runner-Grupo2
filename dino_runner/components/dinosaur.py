from mimetypes import init
from signal import default_int_handler 
import pygame

from dino_runner.utils.constants import RUNNING    

class Dinosaur():
    X_POS = 80
    Y_POS = 310

    def __init__(self) -> None:
        self.image = RUNNING[0]
        self.dino_rect = self.image.get_rect()

        #Definiendo la posicion del Dino
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS

        self.step_index = 0

    def events(self):
        pass
    
    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))

    def run(self):
        self.image = RUNNING[0] if self.step_index < 5 else RUNNING[1]
        self.dino_rect = self.image.get_rect()

        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS

        self.step_index += 1   