import requests

URL_API_LATEST = 'http://api.fixer.io/latest'
BASE_CURRENCY = 'BGN'


def main():

    currency = input("Въведете валута: ")
    currency = currency.upper()

    amount_str = input("Въведете сума: ")
    try:
        amount = float(amount_str)
        if amount < 0:
            print("Поддържат се само суми >= 0!")
            return
    except:
        print("Невалидна стойност!")
        return

    base_currency = input("Въведете валута, към която да се преизчисли сумата: [{}]".format(BASE_CURRENCY))
    base_currency = base_currency.upper()
    if not base_currency:
        base_currency = BASE_CURRENCY

    print("Зареждане на обменни курсове ...")
    rates = get_exchange_rates(base_currency)
    if rates is None:
        print("Обменните курсове не могат да бъдат заредени! "
              "Моля, обърнете се към системния администратор.")
        return

    amount_in_base_currency = calculate_rate_in_base_currency(
        rates,
        currency,
        amount
    )

    if amount_in_base_currency is not None:
        print("Равностойност в {}: {:.2f}".format(
            base_currency,
            amount_in_base_currency
        ))
    else:
        print("Няма информация за посочената валута!")


def calculate_rate_in_base_currency(rates: dict,
                                    currency: str,
                                    amount_in_currency: float) -> float:
    exchange_rate = rates.get(currency, None)
    if exchange_rate is not None:
        return amount_in_currency / exchange_rate
    else:
        return None


def get_exchange_rates(base_currency: str,
                       api_url: str=URL_API_LATEST):
    try:
        response = requests.get(api_url,
                                timeout=20,
                                params={'base': base_currency})
        if response.status_code == 200:
            exchange_rates = response.json()
            rates = exchange_rates.get('rates', {})
            return rates
        else:
            print("Error from server: ", response.status_code)
    except Exception as e:
        print("Error from server! ", str(e))

    return None


if __name__ == '__main__':
    main()

