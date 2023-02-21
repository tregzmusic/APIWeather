import requests
from pprint import pprint
import datetime
import smtplib
from email.mime.text import MIMEText
import time
import local_settings as settings

# https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
# APIKey - 3ef457b391a5bfbc2a713f456084be58
main_link = 'https://api.openweathermap.org/data/2.5/weather'
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.46', 'Accept': '*/*'}

locality = 'Ярославль'   # input('Write name locality:\n')
appid = '3ef457b391a5bfbc2a713f456084be58'

params = {
    'q': locality,
    'appid': appid
}
try:
    while True:
        def send_email(message):
            sender = settings.sender
            password = settings.password

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()

            try:
                server.login(sender, password)
                msg = MIMEText(message)
                msg["Subject"] = 'WEATHER TODAY'
                server.sendmail(sender, sender, msg.as_string())
                return f'The message was sent successfully! {datetime.datetime.now()}'
            except Exception as _ex:
                return f'{_ex}\nCheck your login or password please!'


        response = requests.get(main_link, headers=header, params=params)
        if response.ok:
            data = response.json()
        #   print(f'In the locality {data["name"]} temperature: {round(data["main"]["temp"] - 273.15)} degrees')
            with open('weather.json', 'w', encoding='utf-8') as f:
                f.write(response.text)

        def main():
            message = f'В городе: {data["name"]} температура: {round(data["main"]["temp"] - 273.15)} градусов.\n\nДата ' \
                      f'и время сейчас:\n{datetime.datetime.now()}'  #input('Type your message: ')
            print(send_email(message=message))
            time.sleep(3600)

        if __name__ == '__main__':
            main()

except KeyboardInterrupt:
    print('Goodbye!')
