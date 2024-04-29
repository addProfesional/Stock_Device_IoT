from conexiones import conexiones
import urequests # handles making and servicing network requests
import json

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
        print(self.urlApi)
        data = {
            "username": "FDGFFFF",
            "pass": "uyguyguyhiuy"
        }
        json_data = json.dumps(data)
        headers = {'Content-Type': 'application/json'}
        r = urequests.post(self.urlApi + '/auth/login', data=json_data, headers=headers)
        if r.status_code == 200:
            print("Solicitud POST exitosa!")
            print("Respuesta del servidor:")
            print(r.text)
        else:
            print("Error al enviar la solicitud POST. Código de estado:", r.status_code)

        # Cierra la conexión
        r.close()