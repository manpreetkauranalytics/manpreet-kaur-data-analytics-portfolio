from flask import Blueprint, render_template

main = Blueprint("main", __name__)

@main.route("/")
def home():
    return render_template("home.html")

@main.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")

@main.route("/tableau")
def tableau():
    return render_template("tableau.html")

@main.route("/case-studies")
def case_studies():
    return render_template("case_studies.html")

@main.route("/contact")
def contact():
    return render_template("contact.html")
