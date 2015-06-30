__author__ = 'bdknijf'
import json
import urllib2


new_droplet = {
  "name": "test_api",
  "region": "ams2",
  "size": "512mb",
  "image": "ubuntu-14-04-x64",
  "ssh_keys": "bert",
  "backups": "false",
  "ipv6": "false",
  "user_data": "null",
  "private_networking": "null"
}

url = "https://api.digitalocean.com/v2/droplets"
headers = {'Content-Type': 'application/json',
            'Authorization': 'Bearer 6eb18afa72476ffa38a925eb0223d817c08a8db11d0fc9df371b78093b19fd0d'}

req = urllib2.Request("https://api.digitalocean.com/v2/droplets")
req.add_header('Content-Type', 'application/json')
req.add_header('Authorization', 'Bearer 6eb18afa72476ffa38a925eb0223d817c08a8db11d0fc9df371b78093b19fd0d')

data = json.dumps(new_droplet)

urllib2.urlopen()