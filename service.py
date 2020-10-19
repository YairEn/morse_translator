from flask import Flask, render_template, request, jsonify
import requests

from morse import translate, show_morse_table

app = Flask(__name__)


@app.route("/")
def home():
    placeholder = 'Enter your message here'
    return render_template("index.html", input_placeholder=placeholder)


@app.route("/<name>")
def test(name):
    return render_template("index.html", content=name)


@app.route("/", methods=["POST", "GET"])
def translate_msg():
    placeholder = 'Enter your message here'
    if request.method == "POST":
        data = request.form["msg"]
        placeholder = data
        result = translate(data)
        return render_template("index.html", input_placeholder=placeholder, result=result)
    else:
        return render_template("index.html", input_placeholder=placeholder)


@app.route("/morse_table.html")
def morse_table():
    morse_table_result = show_morse_table()
    return render_template("morse_table.html", morse_table_result=morse_table_result)


@app.route("/check", methods=['POST'])
def user(usr):
    return f"<h1>{usr}</h1>"


if __name__ == "__main__":
    app.run(debug=True)
