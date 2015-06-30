__author__ = 'bdknijf'
import json
import urllib2

from api_token import Token

class Keys:

    def __init__(self, name):
        self.name = name
        self.token = Token('token.json')
        self.token_read = self.token.get_token_read()
        self.headers1 = {'Content-Type': 'application/json',
            'Authorization': 'Bearer %s' % self.token_read}
        self.api_url_sshkeys = "https://api.digitalocean.com/v2/account/keys"

    def get_all_keys(self):
        response = urllib2.urlopen(
            urllib2.Request(self.api_url_sshkeys, headers=self.headers1)
        )
        data = response.read()
        return json.loads(data)

    def get_keys_id(self):
        keys_dict = Keys.get_all_keys(self)
        ssh_keys = keys_dict['ssh_keys']
        result = []
        for i in ssh_keys:
            if i['name'] == self.name:
                result.append(i['id'])
                break
        return result

    def set_key_name(self, name):
        self.name = name
