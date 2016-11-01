import requests

URL_API_LATEST = 'http://api.fixer.io/latest'

try:
    response = requests.get(URL_API_LATEST, timeout=20)
    if response.status_code == 200:
        exchange_rates = response.json()
        rates = exchange_rates.get('rates', {})
        print("EUR/USD: ", rates.get('USD', 'NO DATA'))
        # print(rates)
    else:
        print("Error from server: ", response.status_code)
except Exception as e:
    print("Error from server! ", str(e))
