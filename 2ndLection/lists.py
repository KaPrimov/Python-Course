cmd = ''
prices = []

counter_even_max_prices = 1
counter_even_min_prices = 1
while cmd != "something":
    cmd = (input('Enter a price(or \'stop\'): '))
    if(cmd != 'stop'):
        number = float(cmd)
        prices.append(number)
    else:
        break

prices.sort()


lowest_price = prices[0]
highest_price = prices[-1]

for i in prices:
    if(i == highest_price):
        counter_even_max_prices += 1
    if(i == lowest_price):
        counter_even_min_prices += 1

if (counter_even_max_prices == len(prices) + 1):
    print(print('Average price is:', highest_price))
else:
    check = 0
    while check > -1:
        check += 1
        if(check != counter_even_min_prices):
            prices.remove(lowest_price)
        else:
            break
    prices.sort(reverse=True)
    rcheck = 0
    while rcheck > -1:
        rcheck += 1
        if(rcheck != counter_even_max_prices):
            prices.remove(highest_price)
        else:
            break
    sum = 0
    for price in prices:
        sum += price
    average_price = sum / len(prices)
    print('Average price is:', average_price)
