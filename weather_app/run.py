import requests, json, pprint
from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", title="Home")



if __name__ == "__main__":
    app.run(debug=True)

# BASE_URL="https://api.openweathermap.org/data/2.5/weather?"

# API_KEY="GET YOUR OWN API KEY"
# CITY="Manila"

# URL=BASE_URL + "q=" + CITY + "&appid=" + API_KEY

# r = requests.get(URL)

# if r.status_code == 200:
#     data = r.json()
#     pprint.pprint(data)
#     print(main)
