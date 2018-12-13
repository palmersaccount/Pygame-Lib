# this file is meant for testing the vectors class
from Modules.Vector2 import Vector2

# create vector
vec1 = Vector2(5, 5)

# test str
print(vec1)

# get length and length squared
print(vec1.length())
print(vec1.length_squared())

# get
vec2 = Vector2(3, 3)
print(vec1 + vec2)
