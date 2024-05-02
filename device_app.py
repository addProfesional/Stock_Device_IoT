from mfrc522 import MFRC522
from conexiones import conexiones
from servicio import servicio
import time

srv = servicio()

def enviarLectura(id):
    srv.enviarID(id)


def ejecutar():
    lector = MFRC522(spi_id=0, sck=2, miso=4, mosi=3, cs=1, rst=0)   #Habrá error??
    lector.init()

    conn = conexiones()
    wifi_conectada = conn.conectar_wifi()

    if not wifi_conectada:
        print('No se conectó a ninguna Wifi, terminando...')
        return;

    sesion_es_iniciada = srv.iniciarSesion()
    if not sesion_es_iniciada:
        print('No se inició sesión en el servidor...')
        return

    print("Lector activo...\n")
    while True:
        #lector.init()
        (stat, tag_type) = lector.request(lector.REQIDL)
        if stat == lector.OK:
            (stat, uid) = lector.SelectTagSN()
            if stat == lector.OK:
                identificador = int.from_bytes(bytes(uid), "little", False)
                print("UID: " + str(identificador))
                enviarLectura(str(identificador))
        time.sleep(1.5)