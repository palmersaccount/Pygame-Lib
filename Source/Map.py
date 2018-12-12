import pygame

class Map:
    def __init__(self, width, height, t_w, t_h):
        self.Width = width
        self.Height = height

        self.TILE_WIDTH = t_w
        self.TILE_HEIGHT = t_w

        self.Tiles = []

        for x in range(t_w):
            for y in range(t_h):
                self.Tiles.append(x, y)

    def set_tile(x, y):
        pass

    def get_tile(x, y):
        pass
