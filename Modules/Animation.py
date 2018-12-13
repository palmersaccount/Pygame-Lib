import pygame


def animation_from_texture(texture):
    pass


class Animation:
    def __init__(self, interval=150):
        self.Frames = []
        self.Sources = []
        self.Width = []
        self.Height = []
        self.CurrentFrame = 0
        self.Interval = interval
        self.DeltaTime = 0

    def update(self):
        self.DeltaTime += 1

        if self.DeltaTime % self.Interval == 0:
            self.CurrentFrame += 1

    def draw(self):
        pass
