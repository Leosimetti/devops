# DevOps LAB 1 - Python web application

> A simple one-page app that shows current time in Moscow.

![image](https://user-images.githubusercontent.com/42554566/130326487-4e9b7ab1-3842-4498-9515-881b7939e862.png)

## Built With

- Python
- Flask
- Jinja2
- Gevent
- pytest
- pylint/Dockerfile Linter

## Live Demo

[Live Demo Link](http://10.90.138.134)

## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

Install python and pip

```shell
$ sudo apt install python3 python3-pip python3-venv
```

### Setup

```shell
$ git clone https://github.com/Leosimetti/devops
$ cd devops
```

### Install

```shell
$ cd app_python
$ python3 -m venv venv
$ source venv/bin/activate
$ pip3 install -r requirements.txt
```

### Usage

Set the `PORT` and `HOST_IP` environmental variables to the desired values

```shell
$ cd app_python
$ pyhton3 main.py
```
By default, the application will be available at [http://localhost:5000]() 
### Run tests

```shell
$ pytest
```

## Docker

### Run in Docker
```shell
$ docker pull leosimonetti/devops-lab1-flask
$ docker run -p 5000:5000 leosimonetti/devops-lab1-flask
```

### Build and run tests
```shell
$ cd app_python
$ docker build --target test . 
```

### Build and run
```shell
$ docker build --tag clock_app --target build .
$ docker run -p 5000:5000 clock_app
```

## Author

👤 **Vitaliy Korbashov, BS18-SE-01**

- Innopolis - [v.korbashov@innopolis.university]()
- GitHub: [@Leosimetti](https://github.com/Leosimetti)
- Telegram: [@Leosimonetti](https://t.me/Leosimonetti)
