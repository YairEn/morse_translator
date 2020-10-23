from flask import Flask, render_template, request

from morse import translate, show_morse_table
from loggers import init_logger

app = Flask(__name__)
app_logger = init_logger()


@app.route("/", methods=["POST", "GET"])
def translate_msg():
    placeholder = 'Enter your message here'
    if request.method == "POST":
        data = request.form["msg"]
        placeholder = data
        try:
            result = translate(data)
        except Exception as err:
            result = "Sorry Unknown error ocuured " \
                     "please follow the instructions or contact with us"
            app_logger.fatal(err)
        return render_template("index.html", input_placeholder=placeholder, result=result)
    else:
        return render_template("index.html", input_placeholder=placeholder)


@app.route("/morse_table.html")
def morse_table():
    morse_table_result = show_morse_table()
    return render_template("morse_table.html", morse_table_result=morse_table_result)


if __name__ == "__main__":
    app.run(debug=True)
