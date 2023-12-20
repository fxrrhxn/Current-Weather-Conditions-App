# WeatherApp

🌦️ **Description**:

WeatherApp is a simple Flask web application that allows users to check the current weather for any city worldwide. Powered by the OpenWeatherMap API, it provides temperature, humidity, and more, with support for different units.

🚀 Getting Started

# Prerequisites

- Python 3.x
- Pip (Python package installer)

# Installation

1. Clone the repository:
   
    git clone https://github.com/your-username/WeatherApp.git

3. Navigate to the project directory:

    cd WeatherApp

4. Install dependencies:

    pip install -r requirements.txt

# Usage

1. Set up your OpenWeatherMap API key by creating a `.env` file in the project root:

    API_KEY=your_api_key_here

2. Run the app:

    gunicorn -c gunicorn_config.py weather_app:app

3. Open your browser and visit [http://127.0.0.1:5000](http://127.0.0.1:5000)

# 📝 License

This project is licensed under the [MIT License](LICENSE).
