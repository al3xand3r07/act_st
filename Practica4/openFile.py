from encodings import utf_8
# import glob
#descomentar la linea anterior para usar la función rutaRel()
#Puede tener fallas, ya que solo se estaba desarrollando y no se usa por lo mientras 
"""def rutaRel():
    #ciclo para buscar el archivo en los dispositivos de almacenamiento de windows10
    print("Ingresa el nombre y extension del archivo a codificar:\nPor ejemplo: file.txt")
    nameArch=input(str(":"))   
    abece=["D", "E"]
    Coincidencias=[]
    contABC=0
    i=0
    patNameR='\\**\\'
    nombreRuta=str('C:\\Users\\**\\'+nameArch)
    filepath = glob.glob(nombreRuta, recursive=True)
    if len(filepath)==0:
        varBusq=len(abece)-1
        while contABC!=varBusq:
            unAd=str(abece[i]+':')
            #'~:\**\+' 
            # ~ es la unidad en donde busca
            # ** significa que busca en cada subcarpeta
            # + es el nombre del archivo
            nombreRuta2=str(unAd+patNameR+nameArch)
            filepath = glob.glob(nombreRuta2, recursive=True)
            #borrar esto
            print(filepath)
            for x in filepath:
                Coincidencias.append(x)
            contABC+=1
            i+=1
    elif len(Coincidencias)==0:
        print("El archivo no ha sido encontrado o no existe")
        dirRel=""
        return dirRel
        exit()

    cantidad=len(Coincidencias)-1
    if cantidad>1:
        var=0
        rango=0
        encontrado=False
        for cont in Coincidencias:
            print("\t",var,") ",cont,"")
            var+=1
        while encontrado!=True:
            print("Ingresa el numero del archivo que buscas para cifrar")
            rango=input(int())-1
            if rango>=0 or rango<=cantidad:
                dirRel=Coincidencias[rango]
                encontrado=True
                return dirRel
            if rango<=0 or rango>=cantidad:
                print("El numero ingresado no es valido...!!! :( ") """

#función para leer los datos del archivo
def abrirArchivos(dirArch):
    with open (dirArch, 'rb') as file:
        archivo=file.read()
        file.close
    return archivo