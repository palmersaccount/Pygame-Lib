import pygame
from Modules.Vector2D import Vector2


class Tile:
    def __init__(self, x, y, w, h, img=False):
        self.X = x
        self.Y = y
        self.Position = Vector2(self.X, self.Y)
        self.DestinationRect = [x, y, w, h]
        self.SourceRect = [0, 0, w, h]
        self.UsingImage = img

    def draw(self, window):
        if self.UsingImage:
            pass
        else:
            pygame.draw.rect(window)
