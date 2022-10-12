import base64

def CodArchivo(texto):
    msg="Cifrado listo, revisa tu carpeta... :) "
    txt_Cod=base64.b64encode(texto)
    print("Nota: incluye la extension en el nombre")
    nombreArch=input("Ingresa el nombre del archivo para guardar la codificacion: ")
    with open(nombreArch, 'wb') as file:
        file.seek(0)
        file.write(txt_Cod)
        file.close()
    return msg