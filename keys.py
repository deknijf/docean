__author__ = 'bdknijf'
import json
import urllib2
import pprint

class Keys:

    def __init__(self, name):
        self.name = name
        self.headers1 = {'Content-Type': 'application/json',
            'Authorization': 'Bearer 6eb18afa72476ffa38a925eb0223d817c08a8db11d0fc9df371b78093b19fd0d'}
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
        result = ''
        for i in ssh_keys:
            if i['name'] == self.name:
                result = i['id']
                break

        return result


#response = urllib2.urlopen(
#    urllib2.Request("https://api.digitalocean.com/v2/account/keys", headers=headers1))

#data = response.read()
#dict_data = json.loads(data)
#pprint.pprint(dict_data['ssh_keys'])