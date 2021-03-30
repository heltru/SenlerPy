# SenlerPy

Библиотека на python для работы с api сервиса senler.ru

[![N|Solid](https://img.shields.io/pypi/pyversions/smsactivateru.svg)](https://pypi.python.org/pypi/smsactivateru)

### Установка
Установка с помощью стандартного пакетного менеджера pip:
```
$ pip install senlerpy --upgrade
```
Либо установка напрямую из репозитория, с ручной сборкой
```
$ git clone https://github.com/tezmen/senlerpy
$ cd senlerpy
$ python setup.py install
```
...либо установка через pip но из репозитория, минуя сервера pypi
```
$ pip install git+https://github.com/tezmen/senlerpy
```
### Простой пример
```python
api = Senler('SECRET')

data_send = {
    'count': 1000,
    'date_from': '30.03.2021 01:00:00',
    'date_to': '30.03.2021 15:37:59',
    'vk_user_id[]': [1234325, 45647645],
    'vk_group_id': 99993299
}

data = api(methods.Subscribers.get, data_send)


print(data['items'])
```
Больше примеров смотрите в папке /example/