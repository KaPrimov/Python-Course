import csv
try:
    data_filename = input()

    with open(data_filename, encoding='utf-8') as f:
        reader = csv.reader(f)
        previous_temp = None
        for row in reader:
            current_ts, current_temp = row
            current_temp = float(current_temp)

            if previous_temp is not None:
                if current_temp - previous_temp >= 4:
                    print(current_ts)

            previous_temp = current_temp

except Exception as e:
    print("INVALID INPUT")

