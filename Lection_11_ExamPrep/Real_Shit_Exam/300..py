import csv
import math
from math import hypot

try:
    points_fn = input()
    diff = float(input())
    lines_count = 0
    check = 0

    with open(points_fn, encoding='utf-8') as f:
        previous_coordinate_x = None
        previous_coordinate_y = None
        for line in f:
            lines_count += 1
            line = line.strip()
            line = line.split(',')
            index, x_coord, y_coord = line
            x_coord = float(x_coord)
            y_coord = float(y_coord)

            if previous_coordinate_x is not None:
                if math.hypot(x_coord - previous_coordinate_x, y_coord - previous_coordinate_y) < diff:
                    print(index)
                    check += 1
            previous_coordinate_y = y_coord
            previous_coordinate_x = x_coord

    if check == 0:
        print("NO CLOSE POINTS FOUND; RECORDS COUNT: {}". format(lines_count))

except:
    print("INVALID INPUT")
