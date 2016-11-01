def main():
    try:
        exchange_rates_fn = input()
        amounts_fn = input()

        exchange_rates = load_exchange_rates(exchange_rates_fn)
        amounts = load_amounts(amounts_fn)

        for currency, amount in amounts:
            if currency not in exchange_rates:
                    raise Exception('Currency not found')
            amount_in_bgn = amount / exchange_rates[currency]
            print("{:.2f}".format(amount_in_bgn))
    except:
        print("INVALID INPUT")


def load_exchange_rates(fn: str) -> dict:
    result = {}
    with open(fn, encoding='utf-8') as f:
        for line in f:
            line.strip()
            if line:
                line_parts = line.split(' ')
                currency, rate = line_parts
                rate = float(rate)
                result[currency] = rate
    return result


def load_amounts(fn: str) -> list:
    result = []
    with open(fn, encoding='utf-8') as f:
        for line in f:
            line.strip()
            if line:
                line_parts = line.split()
                amount, currency = line_parts
                amount = float(amount)
                result.append((currency, amount))
    return result


if __name__ == '__main__':
    main()