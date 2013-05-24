from urllib import request
from json import loads

url = 'http://api.worldweatheronline.com/free/v1/weather.ashx?key='
key = 'etrvtzbs6fsqqq2qr4kw5cmg'
url = url + key
url+= '&q=60435&cc&num_of_days=3&format=json'


response = request.urlopen(url)
response = response.readall().decode('utf-8')
json_obj = loads(response)



def getWeather():
    prompt = input("What would you like to know?")
    if "temperature" or "weather" and outside in prompt:
        print('Currently it is', json_obj['data']['current_condition'][0]['weatherDesc'][0]['value'], 'and', json_obj['data']['current_condition'][0]['temp_F'], 'degrees outside')