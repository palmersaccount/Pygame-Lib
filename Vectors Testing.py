# this file is meant for testing the vectors class
from Modules.Vector2D import Vector2D as Vector

# create vectors
vec1 = Vector(5, 5)
vec2 = Vector(3, 3)
vec3 = Vector(5, 5)

# test str
print(vec1)

# get length and length squared
print(vec1.length())
print(vec1.length_squared())

# test addition
print(vec1 + vec2)

# test subtraction
print(vec1 - vec2)

# test multiplication
print(vec1 * 2)
print(vec1 * 8.0)
print(vec1 * vec2)

# test division
print(vec1 / 3.0)

# test tolist and totuple
print(vec1.tolist())
print(vec1.totuple())


# test equality
print(vec1 == vec2)  # False
print(vec1 != vec2)  # True

# compare size
print(vec1 < vec2)  # False
print(vec1 > vec2)  # True
print(vec1 >= vec2)  # True
print(vec1 <= vec2)  # False
