import requests

while True:
    city = input('Enter a city for check weather condition or q for quit: \n')
    if city == 'q':
        break

    url = f'https://api.weatherapi.com/v1/current.json?key=c377e491709c49e49d924101230407&q={city}'

    # print(url)
    url_json = requests.get(url).json()
    location = url_json['location']
    print(f'\nLocation Details of {city}: \n')
    for key,value in location.items():
        print(key,value,sep=' : ')


    current = url_json['current']
    print(f'\nCurrent Details of {city}:\n')
    for key,value in current.items():
        print(key,value,sep=' : ')