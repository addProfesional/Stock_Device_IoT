class session:
    def __init__(self, token=''):
        self.establecerToken(token)

    def establecerToken(self, token=''):
        self.token = token

    def obtenerToken(self):
        return self.token