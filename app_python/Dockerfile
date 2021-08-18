FROM python:3.8-alpine

COPY requirements.txt /
RUN pip3 install --upgrade pip -r requirements.txt

COPY . /app_python
WORKDIR /app_python

CMD ["python3", "app.py"]
