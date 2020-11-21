import pygame
import pygame_menu
from checkers.constants import WIDTH, HEIGHT
from checkers.game import Game
from menu import Menu

FPS = 60
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Checkers")

def main():

    pygame.init()
    menu = Menu(WIN, FPS)
    pygame.quit()

main()