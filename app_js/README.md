# DevOps LAB 1 extra - "COOL CATZ" Javascript web application

> A simple one-page app that displays cool catz.

![image](https://user-images.githubusercontent.com/42554566/130663821-47f8e072-bf89-498b-9e75-b57d75da7d77.png)

## Built With

- Javascript
- express
- Pug (Jade)

## Live Demo

[Live Demo Link](http://10.90.138.134:3000)

## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

Install python and pip

```shell
$ sudo apt install node
```

### Setup

```shell
$ git clone https://github.com/Leosimetti/devops
$ cd devops
```

### Install

```shell
$ cd app_js
$ npm install
```

### Usage

```shell
$ npm start
```

By default, the application will be available at [http://localhost:3000]()

## Docker

### Run

```shell
$ docker pull leosimonetti/devops-lab1-js
$ docker run -p 3000:3000 leosimonetti/devops-lab1-js
```

### Build and run

```shell
$ cd app_js
$ docker build --tag cool_catz .
$ docker run -p 3000:3000 cool_catz
```

## Author

👤 **Vitaliy Korbashov, BS18-SE-01**

- Innopolis - [v.korbashov@innopolis.university]()
- GitHub: [@Leosimetti](https://github.com/Leosimetti)
- Telegram: [@Leosimonetti](https://t.me/Leosimonetti)
