import pygame
import random

from dino_runner.components.power_up.heart_power_up import Heart_power_up
from dino_runner.components.player_hearts.player_heart_manager import PlayerHeartManager

class HeartPowerUpManager:
    def __init__(self):
        self.power_ups=[] 
        self.when_appears = 750
        self.points = 0
        self.option_number = list(range(1,10))
        self.player_heart_manager = PlayerHeartManager()

    def reset_power_ups(self, points):
        self.power_ups=[]   
        self.points = points
        self.when_appears = random.randint(500,1500)+self.points
    def generate_power_ups(self, points):
        self.points = points
        if len(self.power_ups) ==0:
            if self.when_appears == self.points:
                print("generating  powerups")
                self.when_appears = random.randint(self.when_appears +200 , 700 + self.when_appears)
                self.power_ups.append(Heart_power_up())
        return self.power_ups

    def update(self, game, points, game_speed, player):
        self.generate_power_ups(points)
        for power_up in self.power_ups:
            power_up.update(game_speed, self.power_ups)
            if(player.dino_rect.colliderect(power_up.rect)):
                game.player_heart_manager.heart_increase_power_up()
                self.power_ups.pop()


    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen) 