from flask import Flask, render_template
from pip._vendor import requests

requests

app = Flask(__name__)

@app.route('/')
def home():
    home_url = f"https://api.npoint.io/5abcca6f4e39b4955965"
    home_response = requests.get(home_url)
    home_data = home_response.json()
    return render_template("index.html", blogs=home_data)

if __name__ == "__main__":
    app.run(debug=True)
