__author__ = 'bdknijf'

import requests
import json

new_droplet = {
  "name": "testapi",
  "region": "ams2",
  "size": "512mb",
  "image": "ubuntu-14-04-x64",
  "ssh_keys": ["863726"],
  "backups": False,
  "ipv6": False
}

url = "https://api.digitalocean.com/v2/droplets"
headers = {'Content-Type': 'application/json',
            'Authorization': 'Bearer 6eb18afa72476ffa38a925eb0223d817c08a8db11d0fc9df371b78093b19fd0d'}


response = requests.post(url, data=json.dumps(new_droplet, ensure_ascii=False), headers=headers)

print response.status_code
print response.json()
