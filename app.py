from flask import Flask, render_template, request
import requests  # pip install requests
from flask import jsonify

app = Flask(__name__)


# Accueil
@app.route('/')
def index():
    return render_template('index.html')


# METEO
@app.route('/meteo', methods=['GET', 'POST'])
def meteo():
    display = []
    if request.form.get("city_name"):
        display.append(getweather1())
        display.append(getweather2())
        display.append(getweather3())
        return render_template('index.html', display=display)
    else:
        return render_template('index.html')



def getweather1():
    url = 'http://api.weatherapi.com/v1/current.json?key=48b046708754403f8a2185826211210&q={}'
    city_name = request.form['city_name']
    response = requests.get(url.format(city_name)).json()

    display_list = {}
    display_list['API_Name'] = 'Weatherapi.com'
    display_list['city_name'] = city_name

    if 'error' in response:
        display_list['error'] = response['error']['message']
    else:
        display_list['temp'] = response['current']['temp_c']
        display_list['weather'] = response['current']['condition']['text']
        display_list['icon'] = response['current']['condition']['icon']
        print (display_list['icon'])
    return display_list


def getweather2():
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID=42b9eed7b043ca54cb3231dc33db2c69'
    city_name = request.form['city_name']
    response = requests.get(url.format(city_name)).json()

    display_list = {}
    display_list['city_name'] = city_name
    display_list['API_Name'] = 'Openweathermap.org'

    if ('message' in response) and (response['message'] == 'city not found'):
        display_list['error'] = response['message']
    else:
        display_list['temp'] = response['main']['temp']
        display_list['weather'] = response['weather'][0]['description']
        display_list['icon'] = "http://openweathermap.org/img/w/" + response['weather'][0]['icon'] + ".png"
        print(display_list['icon'])
        print(response)
    return display_list


def getweather3():
    city_name = request.form['city_name']
    url = 'http://api.weatherstack.com/current?access_key=ac87dfca7573b17f1f506a88ec89d13f&query={}'
    response = requests.get(url.format(city_name)).json()

    display_list = {}
    display_list['city_name'] = city_name
    display_list['API_Name'] = 'Weatherstack.com'

    if 'success' in response:
        display_list['error'] = response['error']['info']
    else:
        display_list['temp'] = response['current']['temperature']
        display_list['weather'] = response['current']['weather_descriptions'][0]
        display_list['icon'] = response['current']['weather_icons'][0]
        print(display_list['icon'])
    return display_list


if __name__ == '__main__':
    app.run(debug=True)
