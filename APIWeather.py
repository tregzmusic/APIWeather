import requests
from pprint import pprint


# https://api.openweathermap.org/data/2.5/weather     ?    q={city name}   &    appid={API key}
# APIKey - 3ef457b391a5bfbc2a713f456084be58
main_link = 'https://api.openweathermap.org/data/2.5/weather'
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.46', 'Accept': '*/*'}
locality = input('Write name locality:\n')
appid = '3ef457b391a5bfbc2a713f456084be58'

params = {
    'q': locality,
    'appid': appid
}

response = requests.get(main_link, headers=header, params=params)
if response.ok:
    data = response.json()
#   pprint(data)
    print(f'In the locality {data["name"]} temperature: {round(data["main"]["temp"] - 273.15)} degrees')

    with open('weather.json', 'w', encoding='utf-8') as f:
        f.write(response.text)
