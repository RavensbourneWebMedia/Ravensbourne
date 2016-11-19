__author__ = 'Maryam'

from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('template2.html')

@app.route("/", methods=['POST'])
def get_json():
    cityname = request.form['cityname']
    APIkey = "007b9467e4bd58d2a90527fe2532398c"

    response = requests.get("http://api.openweathermap.org/data/2.5/weather?"+"q="+cityname+"&APPID="+APIkey)
    data = response.json()
    weatherInfo= "The temperature in "+str(cityname)+" is "+ str(data['main']['temp']-273.15) + "C"
    return render_template('template2.html', **locals())

# Execute this code when this file is called as a script
if __name__ == "__main__":
    app.run()