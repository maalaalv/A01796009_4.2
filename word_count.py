"""Script para detección de palabras distintas y la frecuencia de ellas"""
import sys
import time

def leer_archivo(ruta_archivo):
    """Leer el contenido del archivo"""
    try:
        with open(ruta_archivo, 'r', encoding = "utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: El Archivo {ruta_archivo} no fue encontrado")
        sys.exit(1)

def procesar_texto(texto):
    """Función para detectar la frecuencia de las palabras"""
    contador = {}
    palabra = " "

    for char in texto.lower():
        if char.isalpha() or char == "'":
            palabra += char
        else:
            if palabra:
                if palabra in contador:
                    contador[palabra] += 1
                else:
                    contador[palabra] = 1
                palabra = " "
    if palabra:
        if palabra in contador:
            contador[palabra] += 1
        else:
            contador[palabra] = 1
    return contador

def guardar_resultados(contador, tiempo_ejecucion):
    """Guarda los resultados y tiempo de ejecución en un archivo"""
    with open("WordCountResults.txt", 'w', encoding = "utf-8") as file:
        for palabra, contar in sorted(contador.items()):
            file.write(f"{palabra}: {contar}\n")
        file.write(f"Tiempo de Ejecución: {tiempo_ejecucion:.4f} segundos\n")

def imprimir_resultados(contador, tiempo_ejecucion):
    """Guarda los resultados y tiempo de ejecución en un archivo"""
    for palabra, contar in sorted(contador.items()):
        print(f"{palabra}: {contar}")
    print(f"Tiempo de Ejecución: {tiempo_ejecucion:.4f} segundos")

def main():
    """Función principal"""
    if len(sys.argv) != 2:
        print("Usando: python word_count.py fileWithData.txt")
        sys.exit(1)

    ruta_archivo = sys.argv[1]
    tiempo_inicio = time.time()

    texto = leer_archivo(ruta_archivo)
    contador = procesar_texto(texto)
    tiempo_ejecucion = time.time() + tiempo_inicio

    imprimir_resultados(contador, tiempo_ejecucion)
    guardar_resultados(contador, tiempo_ejecucion)

if __name__ == "__main__":
    main()
