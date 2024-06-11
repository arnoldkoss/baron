import os
from flask import Flask, render_template, request, flash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/prislista")
def prislista():
    return render_template("prislista.html", page_title="Prislista")


@app.route("/about")
def about():
    return render_template("about.html", page_title="Allt om vår frisersalong")


@app.route("/kontakt", methods=["GET", "POST"])
def kontakt():
    if request.method == "POST":
        flash("Tack {}, vi har tagit emot ditt meddelande!".format(
            request.form.get("name")))
    return render_template("kontakt.html", page_title="Kontakt")





if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=False)