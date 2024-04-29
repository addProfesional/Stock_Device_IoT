from conexiones import conexiones
import urequests # handles making and servicing network requests

class servicio:

    def __init__(self):
        conn = conexiones()
        self.urlApi = conn.obtenerUrlApi()

    def iniciarSesion(self):
        print('Iniciando sesión...')

    def enviarID(self, id_leido):
        print('Enviando el ID: ' +id_leido)

    def testGet(self):
        print('Probando un GET...')
        r = urequests.get('http://date.jsontest.com')
        print(r.content)
        r.close()


    def testPost(self):
        print('Probando un POST...')

