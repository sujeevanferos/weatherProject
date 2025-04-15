from flask import Flask, render_template, request
import requests

app = Flask(__name__)
API_KEY = '66de18540f1101dd242ed50c0abc1bff'

@app.route("/", methods=["GET", "POST"])
def index():
    weather = None
    if request.method == "POST":
        city = request.form.get("city")
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        #https://api.openweathermap.org/data/2.5/weather?q=mumbai&appid=66de18540f1101dd242ed50c0abc1bff
        response = requests.get(url)
        data = response.json()
        if data.get("cod") == 200:
            weather = {
                "city": data["name"],
                "temp": data["main"]["temp"],
                "description": data["weather"][0]["description"]
            }
        else:
            weather = {"error": "City not found"}
    return render_template("index.html", weather=weather)

if __name__ == "__main__":
    app.run(debug=True)
