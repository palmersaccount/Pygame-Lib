import pygame
from Modules.Vector2 import Vector2


class Sprite:
    def __init__(self, img):
        self.Position = Vector2(0, 0)
        self.Velocity = Vector2(0, 0)
        self.Acceleration = Vector2(0, 0)
        self.Texture = img

    def draw(self):
        pass

    def update(self):
        self.Velocity += self.Acceleration
        self.Position += self.Velocity
