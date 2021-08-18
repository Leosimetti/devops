from gevent.pywsgi import WSGIServer
from app_python import create_app
import os

app = create_app()

if __name__ == '__main__':
    PORT = int(os.environ.get("PORT", "5000"))
    HOST_IP = os.environ.get("HOST_IP", "0.0.0.0")

    http_server = WSGIServer((HOST_IP, PORT), app)
    http_server.serve_forever()
