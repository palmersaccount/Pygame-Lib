import math


class Vector2D:
    def __init__(self, x, y):
        self.X = x
        self.Y = y

    # convert to list
    def tolist(self):
        return [self.X, self.Y]

    # convert to tuple
    def totuple(self):
        return (self.X, self.Y)

    # get the length
    def length(self):
        return math.sqrt(self.length_squared())

    # get the length squared
    def length_squared(self):
        return self.X ** 2 + self.Y ** 2

    # override + operator
    def __add__(self, other):
        return Vector2D(self.X + other.X, self.X + other.X)

    # override * operator
    def __mul__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D(self.X * other.X, self.X * other.X)
        else:
            return Vector2D(self.X * other, self.Y * other)

    # override - operator
    def __sub__(self, other):
        return Vector2D(self.X - other.X, self.Y - other.Y)

    # override / operator
    def __truediv__(self, other):
        return Vector2D(self.X / other, self.Y / other)

    # override == operator
    def __eq__(self, other):
        return self.X == other.X and self.Y == other.Y

    # override < operator
    def __lt__(self, other):
        return self.length() < other.length()

    # override <= operator
    def __le__(self, other):
        return self.length() <= other.length()

    # override >= operator
    def __ge__(self, other):
        return self.length() >= other.length()

    # override > operator
    def __gt__(self, other):
        return self.length() > other.length()

    # override != operator
    def __ne__(self, other):
        return not (self.X == other.X and self.Y == other.Y)

    # override str operator
    def __str__(self):
        return "X = " + str(self.X) + ", Y = " + str(self.Y)
