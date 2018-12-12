import pygame

class Tile:
    def __init__(self, x, y, w, h, img=False):
        self.X = x
        self.Y = y
        self.Rect = (x, y, w, h)
        self.UsingImage = img

    def draw(self):
        pass
