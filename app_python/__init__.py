import datetime
import pytz

from flask import Flask, render_template


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def hello_world():
        moscow_time = datetime.datetime.now(pytz.timezone('Europe/Moscow'))
        formatted_time = moscow_time.strftime("%H:%M:%S")

        return render_template("index.html", current_time=formatted_time)

    return app
