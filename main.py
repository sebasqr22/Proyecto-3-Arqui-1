import os

ruta = "/Users/sebastianqr.2208/Desktop/Arqui 1/PROYECTO 3/Iteraciones SPEC/NonCachingSimpleCPU/Branch Predictor/"

#funcion que recibe una ruta de una carpeta, busca el archivo stats.txt. La funcio debe recibir una lista de palabras, cuando en el archivo encuentre una palabra, debe retornar toda la linea
def buscar(ruta, palabras):
    with open(ruta + "/stats.txt") as f:
        for linea in f:
            if any(palabra in linea for palabra in palabras):
                print(linea)

#funcion que con la varibale ruta, busque el archivo runGEM5.sh  La unica entrada de la funcion es la ruta. Debe imprimir el contenido del archivo en forma de lista
def buscar_parametro(ruta, parametros):
    lista = []
    with open(ruta + "/runGEM5.sh") as f:
        for linea in f:
            lista.append(linea)

    #recorrer la lista en la posicion cuatro, hacer un .split para " " e imprimir la lista
    nueva = lista[4].split(" ")
    for i in nueva:
        for parametro in parametros:
            #si i contiene parte de la palabra parametro, imprimir i
            if parametro in i:
                print(i)


def recorrer(lista, parametros):
    for i in range(1,6):

        ruta_nueva = ruta + str(i)
        print(ruta_nueva)
        buscar_parametro(ruta_nueva, parametros)
        buscar(ruta_nueva, lista)
        print("------------------------------------------------------------//------------------------------------------------------------\n\n\n")

#lista = ['system.cpu.dcache.power_state.pwrStateResidencyTicks', 'system.cpu.icache.overallMisses']
lista = ['dcache', 'icache']
parametros = ['l1d_size', 'l1i_size']
recorrer(lista, parametros)