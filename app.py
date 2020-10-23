from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")


@app.route("/terms-conditions.html")
def terms():
    return render_template("/terms-conditions.html")


@app.route("/privacy-policy.html")
def privacy():
    return render_template("privacy-policy.html.html")


if __name__ == "__main__":
    app.run()