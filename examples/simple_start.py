# -*- coding: utf-8 -*-
from senlerpy import Senler, methods

# Создаём объект с секретным ключом
api = Senler('cdfbcf2b72f66eaa65cbb847e619742c5304caa3457445')

# Выполняем запросы к апи используя встроенные схемы
params_subscribers = {
    'count': 1000,
    'date_from': '30.03.2021 01:00:00',
    'date_to': '30.03.2021 15:37:59',
    'vk_user_id[]': [897887, 3557687],
    'vk_group_id': 454367546
}
data = api(methods.Subscribers.get,params_subscribers)
print(data['items'])

# Или прямо указывая URL метода
data = api('utms/get', {'vk_group_id':454367546})
print(data['items'])
#
# Группу ВК можно назначить как для каждого запроса, так и глобально, используя свойство или аргумент конструктора
api = Senler('cdfbcf2b72f66eaa65cbb847e619742c5304caa3457445', vk_group_id=454367546)
data = api(methods.Utms.get)
print(data['items'])
#
api = Senler('cdfbcf2b72f66eaa65cbb847e619742c5304caa3457445')
api.vk_group = 454367546
data = api(methods.Utms.get)
print(data['items'])


data = api(methods.Utms.get)
print(data['items'])