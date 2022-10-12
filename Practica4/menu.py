from sys import exit
import openFile
import encoding
import decoding
#Menu de opciones del programa

def menuCod(opc):
    msgElec="Ingrese una opcion según el numero: "
    msgInv="Opción inválida...!!!"
    while opc!=3:
        print("**********App Codificador - Decodificador**********")
        print("1 -- Codificar")
        print("2 -- Decoficar")
        print("3 -- Salir")
        print(msgElec)
        opc=int(input())

        if opc==1:
            print("--------Codificando--------")
            # DirArchivo=openFile.rutaRel()
            print("NOTA: Los archivos deben estar en la misma carpeta!!!\n")
            DirArchivo=str(input("Ingresa el nombre del archivo:"))
            Lectura=openFile.abrirArchivos(DirArchivo)
            Codificado=encoding.CodArchivo(Lectura)
            print(Codificado)
            
        if opc==2:
            print("--------Decodificando--------")
            print("NOTA: Los archivos deben estar en la misma carpeta!!!")
            print("NOTA2: Los archivos se guardan en la misma carpeta!!!\n")
            DirArchivo=str(input("Ingresa el nombre del archivo a decodificar:"))
            Lectura=openFile.abrirArchivos(DirArchivo)
            Decodificado=decoding.DecodArch(Lectura)
            print(Decodificado)

        if opc==3:
            exit()
        
        if opc<0 or opc>=4:
            print(msgInv)