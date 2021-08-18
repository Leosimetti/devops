FROM python:3.8-slim
WORKDIR /app_python

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY ./src ./src
COPY ./main.py .

CMD ["python3",  "main.py"]

