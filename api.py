from flask import Flask,render_template,request
from weather_api import weather_info

app = Flask(__name__)

@app.route("/", methods= ['GET','POST'])
def home():
    if request.method == 'POST':
        city= request.form['city']
        units= request.form['units']
        infi = weather_info(city,units)
        return render_template('home.html', title="Home Page", info= infi)
    return render_template('home.html',title='Home Page')

@app.route("/about")
def about():
    return render_template("about.html",title="About Page")

@app.route("/contact")
def contact():
    return render_template("contact.html",title="COntact Page")

app.run(debug=True)