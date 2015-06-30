from api_token import Token
from keys import Keys

from pprint import pprint

token = Token('token.json')
token_write = token.get_token()
token_read = token.get_token_read()

keys = Keys('bert')
key_dict = keys.get_keys_id()

print token_write
print token_read
print key_dict
