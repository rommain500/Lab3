
import requests
import datetime
from collections import Counter

class BaseClient:
    # URL vk api
    BASE_URL = 'http://api.vk.com/method/'
    # метод vk api
    method = None
    # GET, POST, ...
    http_method = None

    # Получение GET параметров запроса
    def get_params(self):
        return None

    # Получение данных POST запроса
    def get_json(self):
        return None

    # Получение HTTP заголовков
    def get_headers(self):
        return None

    # Склейка url
    def generate_url(self, method):
        return '{0}{1}'.format(self.BASE_URL, method)

    # Отправка запроса к VK API
    def _get_data(self, method, http_method):


        response = requests.get(self.generate_url(self.method), params=self.get_params())
        print (self.generate_url(self.method))
        return self.response_handler(response)

    # Обработка ответа от VK API
    def response_handler(self, response):
        return response

    # Запуск клиента
    def execute(self):
        return self._get_data(
            self.method,
            http_method=self.http_method
        )


class UserGet(BaseClient):
    method = 'users.get'

    def __init__(self, username):
        self.username = username

    def get_params(self):
        return {
            'user_ids': self.username
        }
    def response_handler(self, response):
       return response.json()['response'][0]['uid']





class FriendsGet(BaseClient):
    method = 'friends.get'

    def __init__(self, userid):
        self.userid = userid

    def get_params(self):
        return {
            'user_id': self.userid,
            'fields': 'bdate'
        }


a = UserGet('prokoshkin_roman').execute()
#b = a.json()
#print (a.json()['response'][0]['uid'])
print (a)
b = FriendsGet(a).execute()
print (b.json())

mas=[]
t=b.json()['response']
for i in t:
    mas.append (i.get('bdate'))

print (mas)

#q = [1,2,3]
#print (len(q))
filt=[]
for i in mas:
    if (i is None):
        continue
    if len(i.split('.')) == 3:
        #print (i.split('.'))
        #print (i.split('.')[2])
        filt.append(i.split('.')[2])

print (filt)

d = Counter(filt)
keys= d.keys()
keys=list(keys)
keys.sort()
for i in keys:
    print(i, ':', '#' * d[i])


