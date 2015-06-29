import json

class Token:
    def __init__(self, token_file):
        self.file = token_file

    def get_token(self):
        with open(self.file) as token_file:
            token = json.load(token_file)
        return token['token']['write']

    def get_token_read(self):
        with open(self.file) as token_file:
            token = json.load(token_file)
        return token['token']['read']