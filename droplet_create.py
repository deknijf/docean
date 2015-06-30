__author__ = 'bdknijf'

import requests
import json

from keys import Keys
from api_token import Token

class DropletCreate:

    def __init__(self, name, region, size, image, ssh_keys, backups=False, ipv6=False, private_networking=False, user_data=None):
        self.name = name
        self.region = region
        self.size = size
        self.image = image
        self.ssh_keys_name = ssh_keys
        self.backups = backups
        self.ipv6 = ipv6
        self.private_networking = private_networking
        self.user_data = user_data

        self.token = Token('token.json')
        self.token_write = self.token.get_token()

        self.keys = Keys(self.ssh_keys_name)
        self.key_id = self.keys.get_keys_id()

        self.url = "https://api.digitalocean.com/v2/droplets"
        self.headers = {'Content-Type': 'application/json',
                        'Authorization': 'Bearer %s' % self.token_write}

    def create(self):
        droplet = {}
        droplet["name"] = self.name
        droplet["region"] = self.region
        droplet["size"] = self.size
        droplet["image"] = self.image
        droplet["ssh_keys"] = self.key_id
        droplet["backups"] = self.backups
        droplet["ipv6"] = self.ipv6
        droplet["user_data"] = self.user_data
        droplet["private_networking"] = self.private_networking

        response = requests.post(self.url, data=json.dumps(droplet, ensure_ascii=False), headers=self.headers)
        return response.status_code, response.json()
