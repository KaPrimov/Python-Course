import math

LOSS_PERCENT = 0.098
LOSS_MULTIPLIER = 1 + LOSS_PERCENT


try:
    sheet_area = float(input())
    box_w = float(input())
    box_h = float(input())
    box_d = float(input())

    box_surface_area = 2 * (
        box_w * box_h + box_w * box_d + box_h * box_d
    )
    box_surface_area *= LOSS_MULTIPLIER

    print(math.ceil(box_surface_area / sheet_area))

except Exception as e:
    print("INVALID INPUT")


