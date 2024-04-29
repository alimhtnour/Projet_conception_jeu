import pygame
from board import *
from costant import *
from copy import deepcopy


class Game:
	def __init__(self, Width, Height, Rows, Cols, Square, Win):
		self.Win = Win
		self.Board = newBoard(Width, Height, Rows, Cols, Square, Win)
		self.Square = Square
		self.select = None
		self.valid_moves = []

	def update_window(self):
		self.Board.draw_Board()
		self.Board.draw_pieces()
		pygame.display.update()


	def reset(self):
		self.Board = newBoard(Width, Height, Rows, Cols, Square, Win)
		self.selected = None
		self.valid_moves = []


	def select(self, row,col):
		if self.select:
			move = self._move(row, col)

			if not move:
				self.select = None
				self.select(row,col)


		piece = self.Board.get_piece(row, col)
		if piece != 0:
			self.select = piece

			self.valid_moves = piece.get_available_move(row, col, self.Board.Board)

	def _move(self, row, col):
		piece = self.Board.get_piece(row,col)

		if piece.image != self.select.image:
			if self.simulate_move(self.select, row, col):
				self.remove(self.Board.Board, self.select, row, col)

				self.Board.move(self.select, row, col)
				self.valid_moves = []
				self.select = None

				return True
			return False
		return False
