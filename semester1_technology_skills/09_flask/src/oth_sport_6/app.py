from flask import Flask, redirect, render_template, request

app = Flask(__name__)

REGISTRANTS = {}

SPORTS = [
  "Frisbee",
  "Fussball",
  "Volleyball",
  "Spikeball",
]

@app.route("/")
def index():
    return render_template("index.html", sports=SPORTS)

@app.route("/register", methods=["POST"])
def register():

    # Validate name
    name = request.form.get("name")
    if not name:
        return render_template("error.html", message="Name fehlt")

    # Validate sport
    sport = request.form.get("sport")
    if not sport:
        return render_template("error.html", message="Sportart fehlt")
    if sport not in SPORTS:
        return render_template("error.html", message="Ungültige Sportart")

    # Remember registrant
    REGISTRANTS[name] = sport

    # Confirm registration
    return redirect("/registrants")


@app.route("/registrants")
def registrants():
    return render_template("registrants.html", registrants=REGISTRANTS)