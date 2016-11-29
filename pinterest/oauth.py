import requests
import json
import urllib


#test access code AaBhWneu3m3u79nphrlY2z0XVoZSFItyW3B0N0VDl27oDaA3lQAAAAA

class pinterest(object):
    def __init__(self,APP_ID,APP_SECRET):
        self.APP_ID=APP_ID
        self.APP_SECRET=APP_SECRET

    def getAuthorizationCode(self,redirect_uri,state=None,scope=['read_public','write_public','read_relationships','write_relationships']):
        payload={'response_type':'code',
                'redirect_uri':redirect_uri,
                'client_id':self.APP_ID,
                'scope':','.join(scope)}

        return 'https://api.pinterest.com/oauth?'+urllib.urlencode(payload)

    def getAccessToken(self,code,uri):
        payload={
            'grant_type':'authorization_code',
            'client_id':self.APP_ID,
            'client_secret':self.APP_SECRET,
            'code':code
        }
        return json.loads(requests.post('https://api.pinterest.com/v1/oauth/token',data=payload).text)
