
from flask import Flask, render_template

app = Flask(__name__)

# Homepage
@app.route("/")
def home():
    return render_template("index.html")


# NEU Lab project page
@app.route("/projects/neu-lab")
def neu_lab():
    return render_template("neu_lab.html")


if __name__ == "__main__":
    app.run(debug=True)


# OmniTrack wearable medical device project
@app.route("/projects/omnitrack")
def omnitrack():
    return render_template("omnitrack.html")

# Independent Mycology Research project
@app.route("/projects/mycology")
def mycology():
    return render_template("mycology.html")

# Hydroponics Research & Development
@app.route("/projects/hydroponics")
def hydroponics():
    return render_template("hydroponics.html")
