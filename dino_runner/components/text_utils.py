import pygame

from dino_runner.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH

FONT_STYLE = "freesansbold.ttf"
black_color = (0, 0, 0)

def get_score_element(point):
    font = pygame.font.Font(FONT_STYLE, 20)
    text = font.render("SCORE: " + str(point), True, black_color)
    text_rect = text.get_rect()
    text_rect.center= [950, 40]

    return text, text_rect

def get_centered_message(message, width = SCREEN_WIDTH // 2, height = SCREEN_WIDTH // 2):
    font = pygame.font.Font(FONT_STYLE, 30)
    text = font.render(message, True, black_color)
    text_rect = text.get_rect()
    text_rect.center = (width, height)

    return text, text_rect