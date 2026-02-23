import requests
from flask import Flask, render_template, abort

app = Flask(__name__, static_folder="static", template_folder="web")

URL = "https://boozeapi.com/api/v1/cocktails"
response = requests.get(URL)

cocktails = []

if response.status_code == 200:
    data = response.json()
    cocktails = data["data"] if "data" in data else data

@app.route("/")
def index():
    return render_template("index.html", cocktails=cocktails)

@app.route("/cocktail/<int:cocktail_id>")
def cocktail_detail(cocktail_id):
    cocktail = next((c for c in cocktails if c["id"] == cocktail_id), None)

    if not cocktail:
        abort(404)

    return render_template("detail.html", cocktail=cocktail)

if __name__ == "__main__":
    app.run(debug=True)
