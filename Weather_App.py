import requests

API_KEY = '3282b53ad8470ea4952e03da26e9bb4c'
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

city = input('Enter your city: ')
request_url = f'{BASE_URL}?appid={API_KEY}&q={city}'
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    print(data)
    weather = data['weather'][0]['main']
    print(f'Weather: {weather}')
    temperature = round(data['main']['feels_like'] - 273.15, 2)
    print(f'Temp: {temperature} celsius')
else:
    print('Error')

input('Press ENTER to exit') 
 
