import math
try:
    side_A = float(input())
    side_B = float(input())
    side_C = float(input())
    p = (side_A + side_B + side_C) / 2

    S = math.sqrt(p * (p - side_A) * (p - side_B) * (p - side_C))

    print("{:.2f}".format(S))

except:
    print("INVALID INPUT")
