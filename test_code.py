from api_token import Token
from keys import Keys
from droplet_create import DropletCreate

token = Token('token.json')
token_write = token.get_token()
token_read = token.get_token_read()

keys = Keys('bert')
key_dict = keys.get_keys_id()

droplet = DropletCreate("test", "ams2", "512mb", "ubuntu-14-04-x64", "bert")
vm = droplet.create()

print token_write
print token_read
print key_dict
print vm

