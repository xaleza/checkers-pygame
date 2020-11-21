import pygame

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS

WHITE = (220, 220, 220)
BLACK = (50,50,50)
BLUE = (0, 0, 255)
GREY = (128, 128, 128)
BROWN = (107,68,35)
YELLOW = (255,228,181)

CROWN = pygame.transform.scale(pygame.image.load('assets/crown.png'), (44,25))
