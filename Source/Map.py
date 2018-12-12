import pygame
from Tile import Tile

class Map:
    def __init__(self, width, height, t_w, t_h):
        self.Width = width
        self.Height = height

        self.TILE_WIDTH = t_w
        self.TILE_HEIGHT = t_w

        self.Tiles = [[Tile(i, j, t_w, t_h) for i in range(width) for j in range(height)]]

    def set_tile(self, x, y):
        pass

    def get_tile(self, x, y):
        pass

    def draw(self):
        for i in tiles
