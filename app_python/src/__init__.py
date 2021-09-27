import datetime

import pytz
from flask import Flask, Response, render_template, request


def create_app():
    app = Flask(__name__)

    def get_moscow_time():
        now = datetime.datetime.now(pytz.timezone("Europe/Moscow"))
        formatted_time = now.strftime("%H:%M:%S")
        return formatted_time

    @app.route("/time")
    def get_time():
        return Response(get_moscow_time(), mimetype="text")

    @app.route("/visits")
    def visits():
        with open("/visits.txt", "r") as f:
            c = f.readlines()
            tag1 = '<span style="white-space: pre-line">'
            return tag1 + "\n".join(c) + "</span>"

    @app.route("/")
    def main_page():
        with open("/visits.txt", "a") as f:
            f.write(f"[{datetime.datetime.now()}] {request.remote_addr} \n")
        return render_template("index.html", current_time=get_moscow_time())

    return app
