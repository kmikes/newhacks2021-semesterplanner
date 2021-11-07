from flask import Flask, redirect, url_for, render_template, request

from datetime import datetime
from typing import Union

### Python Functions
def get_countdown(deadline: str) -> Union[int, str]:
    """ Return the number of days left until the deadline
    >>> get_countdown("16 December, 2021")
    39
    >>> get_countdown("04 November, 2021")
    'This date has already passed!'
    """
    curr_date = datetime.today()
    d2 = datetime.strptime(deadline, "%d %B, %Y")
    # take care of the case if the date is passed
    diff = (d2 - curr_date).days
    if diff >= 0:
        return diff
    return "This date has already passed!"


def get_all_deadlines(user: str, users: dict[str, list]) -> list[str]:
    """ Return all deadlines for a specific user"""
    deadlines = []
    if len(users[user]) > 0:
        for date in users[user]:
            countdown = get_countdown(date)
            deadlines.append(countdown)
    return deadlines

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
    #return render_template("index.html")

    count_to_xmas = get_countdown("25 December, 2021")

    if request.method == "POST":
        user = request.form["nm"]
    else:
        return  render_template("index.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("user", usr=user))
    else:
        return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)
