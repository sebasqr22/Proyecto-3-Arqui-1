import os

ruta = "/Users/sebastianqr.2208/Desktop/Arqui 1/PROYECTO 3/Iteraciones SPEC"

#funcion que tome la variable archivos de la funcion leer_archivos y reciba una lista de strings que se llame lista_buscar y busque cada string de lista_buscar en la matriz y devuelva esa linea de cada matriz
def buscar_linea(archivos, lista_buscar):
    lineas = []
    for archivo in archivos:
        for linea in archivo:
            for string in lista_buscar:
                if string in linea:
                    lineas.append(linea)
    return lineas

#funcion que toma la variable ruta y lee todos los archivos que hay en las carpetas dentro de la ruta, los archivos se llaman stats.txt y los retorna en una matriz. Ademas, debe de guardar el nombre de la carpeta que esta leyendo
def leer_archivos():
    archivos = []
    for carpeta in os.listdir(ruta):
        if os.path.isdir(os.path.join(ruta, carpeta)):
            for archivo in os.listdir(os.path.join(ruta, carpeta)):
                if archivo == "stats.txt":
                    with open(os.path.join(ruta, carpeta, archivo), "r") as file:
                        archivos.append([carpeta, file.readlines()])
    return archivos


#funcion main que llama a las funciones leer_archivos y buscar_linea y luego recorrera lo que retorna buscar_linea y lo imprimira
def main():
    archivos = leer_archivos()
    lista_buscar = ["BTB"]
    lineas = buscar_linea(archivos, lista_buscar)
    for linea in lineas:
        print(linea)

main()