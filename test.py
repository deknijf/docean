class Token:
    """"
    some information
    """"
    import configparser

    def get_token():
        settings = configparser.ConfigParser()
        settings._interpolation = configparser.ExtendedInterpolation()
        settings.read('token.ini')
        token = settings.get('digital_ocean', 'token')
        return token

    def __init__(self):
        self.get_token()