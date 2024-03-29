from flask import Flask, render_template, request

from loggers import init_logger
from morse import show_morse_table, translate

app = Flask(__name__)
app_logger = init_logger()


@app.route("/", methods=["POST", "GET"])
def translate_msg():
    """
    Home page get the message to translate
    :return: index.html template with the translated message
    """
    placeholder = 'Enter your message here'
    if request.method == "POST":
        data = request.form["msg"]
        placeholder = data
        try:
            result = translate(data)
        except Exception as err:
            result = ("Sorry Unknown error occurred "
                      "please follow the instructions or contact with us")
            app_logger.fatal(err)
        return render_template("index.html", input_placeholder=placeholder, result=result)
    else:
        return render_template("index.html", input_placeholder=placeholder)


@app.route("/morse_table.html")
def morse_table():
    """
    Show the morse tables
    :return: morse_table.html template with all the morse tables ("A": ".-")
    that the app supported
    """
    morse_table_result = show_morse_table()
    return render_template("morse_table.html", morse_table_result=morse_table_result)


if __name__ == "__main__":
    app.run()
