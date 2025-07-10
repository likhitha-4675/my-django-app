from app import app
from flask import render_template, request

@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/submit", methods=["POST"])
def submit():
    name=request.form["username"]
    return render_template("result.html", name=name)