# -*- coding: utf-8 -*-
import requests
import hashlib
from .exceptions import HttpError
from . import __version__, __api_version__


class RequestApi:
    __base_url = 'https://senler.ru/api/'

    def __init__(self, secret):
        self.__session = requests.Session()
        self.__secret = str(secret).strip()
        self.__session.headers['User-Agent'] = f'SenlerPythonClient/{__version__}'

    def _calculate_hash(self, params):
        values = str()
        for key in params.keys():
            item = params[key]
            if isinstance(item, list) or isinstance(item, tuple):
                values += ''.join(str(x) for x in item)
            else:
                values += str(item)
        values += self.__secret

        return hashlib.md5(values.encode('utf-8')).hexdigest()

    def send(self, method_name, params=None):

        if params is None:
            params = {}
        params['v'] = str(__api_version__)
        params['hash'] = self._calculate_hash(params)

        url = self.__base_url + str(method_name)

        try:
            result = self.__session.post(url, params, timeout=300)
        except (ConnectionError, TimeoutError, requests.exceptions.ReadTimeout):
            raise HttpError('Error with connection to senler.ru API server')
        if result.status_code == 404:
            raise HttpError(f'Method {method_name} not found!')
        return result

    @property
    def url(self):
        return self.__base_url
