import csv
# try:
stocks_fn = input()

percent_diff = float(input())
lines_count = 0
check = 0

with open(stocks_fn, encoding='utf-8') as f:
    reader = csv.reader(f)
    previous_percentage = None
    for row in reader:
        lines_count += 1
        current_ts, current_percentage = row
        current_percentage = float(current_percentage)

        if previous_percentage is not None:
            if current_percentage - previous_percentage > percent_diff:
                print("{} {}".format(current_ts, (current_percentage / previous_percentage) ))
                check += 1

        previous_percentage = current_percentage

if check == 0:
    print("NO DRASTIC CHANGES; RECORDS COUNT: {}".format(lines_count))
# except Exception as e:
#     print("INVALID INPUT")
#     print(e)
