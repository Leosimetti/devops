from app_python import create_app
import os

app = create_app()

if __name__ == '__main__':
    PORT = os.environ.get("PORT", "5000")
    HOST_IP = os.environ.get("HOST_IP", "0.0.0.0")

    app.run(host=HOST_IP, port=PORT)
