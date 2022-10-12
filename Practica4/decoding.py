import base64
def DecodArch(texto):
    msg="Archivo decodificado con éxito :)"
    txt_Cod = base64.b64decode(texto)
    print("Incluye el formato del archivo ( .docs | .png | .jpg | entre otros)")
    nombreArch=input("Ingresa el nombre del archivo para guardar la decodificacion: ")
    with open(nombreArch, 'wb') as file:
        file.seek(0)
        file.write(txt_Cod)
        file.close()
    return msg