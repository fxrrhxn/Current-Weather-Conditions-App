from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv

app = Flask(__name__, template_folder='templates', static_folder='static')
load_dotenv()

# Mapping of unit codes to user-friendly names
UNIT_NAMES = {
    'metric': 'Celsius',
    'imperial': 'Fahrenheit',
    'standard': 'Kelvin',
}

@app.route('/', methods=['GET', 'POST'])
def get_current_weather():
    if request.method == 'POST':
        city = request.form['city']
        units = request.form['units']

        api_key = os.getenv('API_KEY')
        if not api_key:
            return render_template('index.html', error="API key not found. Please check your configuration.")

        request_url = f"https://api.openweathermap.org/data/2.5/weather?appid={api_key}&q={city}&units={units}"

        try:
            weather_data = requests.get(request_url).json()

            # Check if the API request was successful
            if 'main' in weather_data and 'temp' in weather_data['main']:
                return render_template('index.html', weather=weather_data, units=units, unit_name=UNIT_NAMES.get(units, units.capitalize()))
            else:
                error_message = f"Unable to fetch weather data for {city}. Please check the city name and try again."
                return render_template('index.html', error=error_message)

        except requests.RequestException as error:
            return render_template('index.html', error=f"An error occurred: {error}")

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
