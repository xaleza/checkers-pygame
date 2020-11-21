import pygame
import pygame_menu
from checkers.constants import WIDTH, HEIGHT
from checkers.game import Game

class Menu:
    def __init__(self, win, fps):
        self.win = win
        self.fps = fps
        self.mytheme = pygame_menu.themes.THEME_DEFAULT.copy()
        self.myimage = pygame_menu.baseimage.BaseImage(image_path="assets/background.jpg",drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL)
        self.mytheme.background_color = self.myimage
        self.mytheme.widget_font = pygame_menu.font.FONT_OPEN_SANS_BOLD
        self.menu = pygame_menu.Menu(WIDTH,HEIGHT, 'Checkers', theme=self.mytheme)
        self.init()
    
    def init(self):
        self.menu.add_button('Play', self.start_the_game)
        self.menu.add_button('Quit', pygame_menu.events.EXIT)
        self.menu.mainloop(self.win)

    def start_the_game(self):
        run = True
        clock = pygame.time.Clock()
        game = Game(self.win)
        while run:
            clock.tick(self.fps)

            if game.winner() != None:
                print(game.winner())
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    game.select(pos)

            game.update()