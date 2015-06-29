from api_token import Token

token = Token('token.json')
token_write = token.get_token()
token_read = token.get_token_read()

print token_write
print token_read
