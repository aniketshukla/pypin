import requests
import json
import urllib


class boards(object):
    def __init__(self,code):
        self.code=code
        self.uri="https://api.pinterest.com/v1/boards/"

    def create_board(self,name,description):
        params={
        'name':name,
        'description':description,
        'access_token':self.code
        }

        return json.loads(requests.post(self.uri,data=params).text)
