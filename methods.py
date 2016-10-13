from base import BaseClient

class UserGet(BaseClient):
    BASE_URL = "https://api.vk.com/method/"

    method = "users.get"

    def __init__(self, username):
        self.username = username

    def get_params(self):
        return{
            "user_ids": self.username
        }

    def response_handler(self, response):
        b = response.json()
        return b['response'][0]['uid']


class FriendsGet(BaseClient):
    BASE_URL = "https://api.vk.com/method/"

    method = "friends.get"

    def __init__(self, username):
        self.username = username

    def get_params(self):
        return{
            "user_id": self.username,
            "fields": "bdate"
        }

    def response_handler(self, response):
        data = response.json()
        res = {}
        for i in data['response']:
            try:
                if i["bdate"].split('.')[2] in res.keys():
                    res[i["bdate"].split('.')[2]] += 1
                else:
                    res[i["bdate"].split('.')[2]] = 1
            except:
                pass
        return res

