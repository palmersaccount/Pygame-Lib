#import pygame


class Tile:
    def __init__(self, x, y, w, h, img=False):
        self.X = x
        self.Y = y
        self.DestinationRect = [x, y, w, h]
        self.SourceRect = [0, 0, w, h]
        self.UsingImage = img

    def draw(self, window):
        if self.UsingImage:
            pass
        # else:
            # pygame.draw.rect(window)
