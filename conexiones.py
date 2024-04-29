import network
import config
import time

class conexiones:

    def __init__(self, ssid=config.DEFAULT_SSID, password=config.DEFAULT_PASS_WIFI):
        self.ssid = ssid
        self.password = password

        self.apihost = config.HOST_API
        self.enableSSL = config.ENABLE_SSL

        self.wlan = network.WLAN(network.STA_IF)

    '''def conectar_wifi(self):
        print('Conectando a la red Wifi...')
        self.wlan.active(True)
        self.wlan.connect(self.ssid, self.password)
        print('Se conectó a Wifi')'''

    def conectar_wifi(self):
        print('Conectando a la red Wifi...')
        self.wlan.active(True)
        self.wlan.connect(self.ssid, self.password)

        start_time = time.time()
        while not self.wlan.isconnected():
            if time.time() - start_time >= config.TIMEOUT_WIFI_CONNECT:
                print('No se pudo conectar a la red: ' +self.ssid)
                return False
            time.sleep(1)

        print('Se conectó a la red Wifi: ' +self.ssid)
        return True

    def obtenerUrlApi(self):
        protocolo = 'http://' if not self.enableSSL else 'https://'
        return protocolo + self.apihost + '/'

    def imprimirUnaVariable(self):
        print(config.HOST_API)

