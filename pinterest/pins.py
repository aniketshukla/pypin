import requests
import json
import urllib



class pins(object):
    def __init__(self,code):
        self.code=code
        self.uri="https://api.pinterest.com/v1/pins/"

    def create_pins(self,username,board,note,image_url,link=None):
        params={
        'board':username+"/"+board,
        'note':note,
        'image_url':image_url,
        'access_token':self.code
        }
        if link is not None:
            parameters["link"]=link

        return json.loads(requests.post(self.uri,data=params).text)
