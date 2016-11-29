import requests
import json
import urllib


class user(object):
    def __init__(self,code):
        self.code=code
        self.uri="https://api.pinterest.com/v1/me/"

    def fetch_user_data(self):
        return json.parse(requests.get(self.uri,params={'access_token':self.code}).text)
