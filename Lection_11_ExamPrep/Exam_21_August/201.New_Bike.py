import math

try:
    price_bike = float(input())
    savings = float(input()) * 10
    spendings = float(input())

    if savings > spendings:
        bike_fund = (savings - spendings) / 10
        day = math.ceil(price_bike / bike_fund)
        print(day)
    else:
        print("NO BIKE FOR YOU")

except Exception as e:
    print("INVALID INPUT")

