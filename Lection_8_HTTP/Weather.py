import requests
from datetime import datetime

URL_API_LATEST = 'http://api.openweathermap.org/data/2.5/weather'
BASE_CITY = 'Sofia'
APPID = '965acdac1ae64cf06761bb563ad34d96'


def main():

    city = input("Въведете град: ")
    weather = get_data(city, URL_API_LATEST)
    ts = weather[1]
    dt = datetime.fromtimestamp(ts)
    temp_humidity_pressure = weather[0]
    fahrenheit_temp = float(temp_humidity_pressure['temp'])
    celsius_temp = (fahrenheit_temp - 32) * 5/9
    wind_data = weather[2]
    print("Информация към: ", dt)
    print("Температура: {:.2f}".format(celsius_temp))
    print("Налягане: ", temp_humidity_pressure['pressure'])
    print("Влажност: ", temp_humidity_pressure['humidity'])
    print("Вятър {} м/с".format(wind_data['speed']))


def get_data(city: str,
            api_url: str=URL_API_LATEST):
    try:
        response = requests.get(api_url,
                                timeout=20,
                                params={'q': city,
                                        'appid': APPID})
        if response.status_code == 200:
            weather_data= response.json()
            temp_pressure_humidity = weather_data.get('main', {})
            date = weather_data.get('dt', {})
            wind_data = weather_data.get('wind', {})
            return temp_pressure_humidity, date, wind_data
        else:
            print("Error from server: ", response.status_code)
    except Exception as e:
        print("Error from server! ", str(e))

    return None


if __name__ == '__main__':
    main()

