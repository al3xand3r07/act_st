import subprocess
import sys

def consulta():
    comando = "ipconfig /displaydns"
    consulta = subprocess.run(comando, stdout=subprocess.PIPE)
    guardarArchivo(consulta.stdout)
    print("Informe DNS generado con éxito")

def guardarArchivo(result):
    try:
        with open('reporteCachéDNS.txt', 'wb') as file:
            file.write(result)
        file.close()
    except Exception as error:
        print("No se pudo generar el reporte: " + str(error))

if __name__=='__main__':
    consulta()