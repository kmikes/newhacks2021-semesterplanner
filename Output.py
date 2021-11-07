from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Semester Countdown. Input your deadlines to stay motivated"

if __name__ == "__main__":
    app.run()

