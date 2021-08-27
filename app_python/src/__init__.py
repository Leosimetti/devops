import datetime

import pytz
from flask import Flask, Response, render_template


def create_app():
    app = Flask(__name__)

    def get_moscow_time():
        now = datetime.datetime.now(pytz.timezone("Europe/Moscow"))
        formatted_time = now.strftime("%H:%M:%S")
        return formatted_time

    @app.route("/time")
    def get_time():
        return Response(get_moscow_time(), mimetype="text")

    @app.route("/")
    def main_page():
        return render_template("index.html", current_time=get_moscow_time())

    return app
