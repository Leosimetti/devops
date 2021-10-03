FROM python:3.8-slim as base
WORKDIR /app_python

COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY ./src ./src

FROM base as test
COPY ./conftest.py .
COPY ./testing ./testing
RUN ["pytest"]

FROM base as build
COPY ./main.py .
RUN adduser tolya && chown -R tolya main.py
USER tolya
EXPOSE 5000
CMD ["python3",  "main.py"]
