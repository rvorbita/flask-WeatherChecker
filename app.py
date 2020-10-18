import requests, json, pprint
from flask import Flask, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy

#APP
app=Flask(__name__)
#DATABASE
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///weather.db'
db=SQLAlchemy(app)

#DBModel

class City(db.Model):
    """city model"""
    id=db.Column(db.Integer, primary_key=True)
    city=db.Column(db.String(90), nullable=False)


@app.route('/', methods=['GET', 'POST'])
def index():

    #get a new city from the form
    if request.method == 'POST':
        new_city=request.form.get('city')
        if new_city:
            new_city_obj=City(city=new_city)
            db.session.add(new_city_obj)
            db.session.commit()
         
    cities = City.query.all()

    weather_data = []

    for city in cities:
        
        BASE_URL="https://api.openweathermap.org/data/2.5/weather?"

        API_KEY="125586a42d0bd62391a4b2c4b3c59057"
        CITY= "Manila"

        # URL=BASE_URL + "q=" + CITY + "&appid=" + API_KEY
        URL=f"{BASE_URL}q={city.city}&appid={API_KEY}"

        r = requests.get(URL).json()
        
        weather={
            'city': city.city,
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon']
        }

        weather_data.append(weather)
            

    return render_template("index.html", weather_data=weather_data, title="Home")

if __name__ == "__main__":
    app.run(debug=True)