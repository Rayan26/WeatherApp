from flask import Flask, render_template, request
import requests  # pip install requests
from flask import jsonify

app = Flask(__name__)


#Premiere API
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city_name = request.form['city_name']

        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID=42b9eed7b043ca54cb3231dc33db2c69'
        response = requests.get(url.format(city_name)).json()

        temp = response['main']['temp']
        weather = response['weather'][0]['description']
        min_temp = response['main']['temp_min']
        max_temp = response['main']['temp_max']
        icon = response['weather'][0]['icon']

        print(temp, weather, min_temp, max_temp, icon)
        return render_template('index.html', temp=temp, weather=weather, min_temp=min_temp, max_temp=max_temp,
                               icon=icon, city_name=city_name)
    else:
        return render_template('index.html')


#Deuxieme API
@app.route('/getweather', methods=['GET', 'POST'])
def getweather():
    if request.method == 'POST':
        city_name = request.form['city_name']
        url = 'http://api.weatherapi.com/v1/current.json?key=48b046708754403f8a2185826211210&q={}'
        response = requests.get(url.format(city_name)).json()

        temp = response['current']['temp_c']
        weather = response['current']['condition']['text']
        min_temp = response['current']['temp_c']
        max_temp = response['current']['temp_f']
        icon = response['current']['condition']['icon']
        print(temp, weather, min_temp, max_temp, icon)
        return render_template('index.html', temp=temp, weather=weather, min_temp=min_temp, max_temp=max_temp,
                               icon=icon, city_name=city_name)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
