user_input = input()
numbers = []
user_input = user_input.strip()
user_input = user_input.split(' ')

for symbol in user_input:
    if symbol is not '':
        number = int(symbol)
        numbers.append(number)
    else:
        continue
check = 1
for integer in numbers:

    if numbers[check] > numbers[check - 1]:
        check += 1
        if check == len(numbers):
            print("SORTED")
            break
    else:
        print(check)
        break
