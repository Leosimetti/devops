from gevent.pywsgi import WSGIServer
from src import create_app
import os

if __name__ == '__main__':
    app = create_app()

    PORT = int(os.environ.get("PORT", "5000"))
    HOST_IP = os.environ.get("HOST_IP", "0.0.0.0")

    http_server = WSGIServer((HOST_IP, PORT), app)
    http_server.serve_forever()
