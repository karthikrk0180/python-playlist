import math


def circle_stats(radius):
    area = math.pi * radius ** 2
    circum = 2 * math.pi * radius
    return area, circum

a, c = circle_stats(3)

a.__round__(2)
print("Area: ", round(a,2), "Circumfernce: ", round(c,2))