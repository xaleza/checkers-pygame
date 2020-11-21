import pygame
from .constants import BLACK, WHITE, ROWS, COLS, SQUARE_SIZE, GREY, CROWN

class Piece:
    PADDING = 20
    OUTLINE = 5

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        self.x = 0
        self.y = 0
        self.calc_pos()
    
    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2
    
    def make_king(self):
        self.king = True

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()

    def draw(self, win, turn):
        radius = SQUARE_SIZE // 2 - self.PADDING
        if self.color == turn:
            pygame.draw.circle(win, WHITE, (self.x, self.y), radius + self.OUTLINE + 5) 
        pygame.draw.circle(win, GREY, (self.x, self.y), radius + self.OUTLINE) 
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)
        if self.king:
            win.blit(CROWN, (self.x-CROWN.get_width()//2, self.y-CROWN.get_height()//2))

    def __repr__(self):
        return str(self.color)
    