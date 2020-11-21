import pygame
from checkers.board import Board
from .constants import BLACK, WHITE, BLUE, SQUARE_SIZE, ROWS, COLS

class Game:
    def __init__(self, win):
        self._init()
        self.win = win

    def update(self):
        self.board.draw(self.win, self.turn)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = WHITE
        self.valid_moves = {}

    def reset(self):
        self._init()

    def select(self, pos):
        x, y = pos
        row = y // SQUARE_SIZE
        col = x // SQUARE_SIZE
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(pos)
        
        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True
            
        return False

    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.board.remove(skipped)
            self.change_turn()
        else:
            return False
        
        return True

    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, BLUE, (col * SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2), 15)

    def change_turn(self):
        self.valid_moves = []
        if self.turn == WHITE:
            self.turn = BLACK
        else:
            self.turn = WHITE

    def winner(self):
        return self.board.winner()

    def draw(self):
        for row in self.board.board:
            for piece in row:
                if piece != 0 and piece.color == self.turn and len(self.board.get_valid_moves(piece)) > 0:
                    return self.draw 
        self.draw = True
        return self.draw 

    def get_board(self):
        return self.board
    
    def highlight_move(self, new_board):
        old_board = self.board
        for row in range(ROWS):
            for col in range(COLS):
                if old_board.board[row][col] == 0 and new_board.board[row][col] != 0:
                    pygame.draw.circle(self.win, BLUE, (col * SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2), 40, width = 5)
                if new_board.board[row][col] == 0 and old_board.board[row][col] != 0:
                    pygame.draw.circle(self.win, BLUE, (col * SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2), 40, width = 5)
        pygame.display.update()

    def ai_move(self, new_board):
        self.highlight_move(new_board)
        pygame.time.delay(1000)
        self.board = new_board
        self.change_turn()