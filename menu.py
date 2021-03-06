import pygame
import pygame_menu
from checkers.constants import WIDTH, HEIGHT, WHITE, BLACK
from checkers.game import Game
from minimax.algorithm import minimax
import time

class Menu:
    def __init__(self, win, fps):
        self.win = win
        self.fps = fps
        self.mytheme = pygame_menu.themes.THEME_DEFAULT.copy()
        self.myimage = pygame_menu.baseimage.BaseImage(image_path="assets/background.jpg",drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL)
        self.mytheme.background_color = self.myimage
        self.mytheme.widget_font = pygame_menu.font.FONT_OPEN_SANS_BOLD
        self.menu = pygame_menu.Menu(WIDTH,HEIGHT, 'Checkers', theme=self.mytheme)
        self.winner_screen = pygame_menu.Menu(WIDTH,HEIGHT, 'Checkers', theme=self.mytheme)
        self.menu_ai = pygame_menu.Menu(WIDTH,HEIGHT, 'Checkers', theme=self.mytheme)
        self.ai_difficulty = 1
        self.init()
    
    def init(self):
        self.menu.add_button('Play against the Computer', self.open_menu_ai)
        self.menu.add_button('Play Local Multiplayer', self.start_the_game)
        self.menu.add_button('Quit', pygame_menu.events.EXIT)
        self.menu.mainloop(self.win)

    def start_the_game(self):
        run = True
        clock = pygame.time.Clock()
        game = Game(self.win)
        while run:
            clock.tick(self.fps)

            if game.winner() != None:
                self.print_winner(game.winner())
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    game.select(pos)

            game.update()
    
    def open_menu_ai(self):
        self.menu_ai.add_selector('Difficulty: ', [('Beginner', 1),('Easy', 2),('Hard', 5)], onchange=self.set_ai_difficulty)
        self.menu_ai.add_button('Start', self.start_the_game_ai)
        self.menu_ai.add_button('Quit', pygame_menu.events.EXIT)
        self.menu_ai.mainloop(self.win)

    
    def set_ai_difficulty(self, selected, value):
        self.ai_difficulty = value

    def start_the_game_ai(self):
        run = True
        clock = pygame.time.Clock()
        game = Game(self.win)
        while run:
            clock.tick(self.fps)

            if game.turn == BLACK:
                value, new_board = minimax(game.get_board(), self.ai_difficulty, BLACK, game)
                game.ai_move(new_board)

            if game.winner() != None:
                self.print_winner(game.winner())
            
            if game.draw():
                print("draw")
                run = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    game.select(pos)

            game.update()
    
    def print_winner(self, winner_color):
        if winner_color == WHITE:
            winner = 'White'
        else:
            winner = 'Black'

        winner_text = winner + ' wins!'
        self.winner_screen.add_label(winner_text, max_char=-1, font_size=60)
        self.winner_screen.add_button('Quit', pygame_menu.events.EXIT)
        self.winner_screen.mainloop(self.win)

