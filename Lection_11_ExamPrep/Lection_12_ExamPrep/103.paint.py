import math

COVER_AREA = 1.76

try:
    w = float(input())
    h = float(input())
    area = w * h

    number_of_tubes = math.ceil(area / COVER_AREA)

    print(number_of_tubes)
except:
    print("INVALID INPUT")