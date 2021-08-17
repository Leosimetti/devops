FROM python:3.8-alpine
COPY . ./app_python
WORKDIR /app_python
COPY requirements.txt /app_python
RUN pip3 install --upgrade pip -r requirements.txt

CMD python3 app.py
