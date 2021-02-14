from flask import Flask, render_template
import random
from datetime import date
import requests


app = Flask(__name__)

@app.route('/')
def home():
    current_year = date.today()
    this_year = current_year.year
    random_number = random.randint(0, 10)
    return render_template("index.html", num=random_number, year=this_year)

@app.route('/guess/<name>')
def guess_page(name):
    gender_url = f"https://api.genderize.io?name={name}"
    gender_response = requests.get(gender_url)
    gender_data = gender_response.json()
    gender = gender_data["gender"]
    age_url = f"https://api.agify.io?name={name}"
    age_response = requests.get(age_url)
    age_data = age_response.json()
    age = age_data["age"]
    return render_template("guess.html", name=name, gender=gender, age=age)

@app.route("/blog/<num>")
def get_blog(num):
    blog_url = f"https://api.npoint.io/5abcca6f4e39b4955965"
    blog_response = requests.get(blog_url)
    blog_data = blog_response.json()
    return render_template("blog.html", blogs=blog_data)
if __name__ == "__main__":
    app.run(debug=True)


