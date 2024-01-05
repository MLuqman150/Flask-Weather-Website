from flask import Flask, request, render_template
from weather import getCurrentWeather
from waitress import serve

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/weather")
def get_weather():
    city = request.args.get("city")
    # Check for empty values
    if not bool(city.strip()):
        city = "Bahawalpur"

    weather_data = getCurrentWeather(city)

    if not weather_data['cod'] == 200:
        return render_template('cityNotFound.html')
    
    return render_template(
        "weather.html",
        title = weather_data["name"],
        status = weather_data["weather"][0]["description"].capitalize(),
        temp = f"{weather_data['main']['feels_like']:.2f}",
        feels_like = f"{weather_data['main']['feels_like']:.2f}"
    )

if __name__ == "__main__":
    # runing app on the local host
    # app.run(host="0.0.0.0", port=5000)
    serve(app, host="0.0.0.0", port=5000)
    