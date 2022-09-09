import pygame
from tkinter import image_names
from pygame.sprite import Sprite

class Titles(Sprite):
    def __init__(self, image):
        self.image = image
        self.rect = self.image.get_rect()

    def draw(self, screen):
        screen.blit(self.image, self.rect)