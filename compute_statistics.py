"""Script para obtener medidas estadísticas básicas"""
import sys
import time

def leer_archivo(ruta_archivo):
    """Leer numeros de un archivo, procurando ignorar datos invalidos."""
    numeros = []
    try:
        with open(ruta_archivo, 'r', encoding="utf-8") as file:
            for line in file:
                try:
                    num = float(line)
                    numeros.append(num)
                except ValueError:
                    print(f"Datos ignorados: {line.strip()}")
    except FileNotFoundError:
        print("Archivo no encontrado")
        sys.exit(1)
    return numeros

def obtener_media(datos):
    """Se realiza función para obtener la media de una lista de numeros"""
    return sum(datos) / len(datos) if datos else 0

def obtener_mediana(datos):
    """Se realiza función para obtener la mediana de una lista de numeros"""
    datos_ordenados = sorted(datos)
    n = len(datos_ordenados)
    mid = n // 2

    if n % 2 == 0:
        return (datos_ordenados[mid - 1] + datos_ordenados[mid]) / 2
    return datos_ordenados[mid]

def obtener_moda(datos):
    """Realizar función para obtener la moda de una lista de numeros"""
    frecuencia = {}
    for num in datos:
        frecuencia[num] = frecuencia.get(num, 0) + 1
    max_frec = max(frecuencia.values())
    modas = [num for num, frec in frecuencia.items() if frec == max_frec]
    return modas if len(modas) > 1 else modas[0]

def obtener_varianza(datos, media):
    """Realizar función para obtener la varianza de una lista de numeros"""
    return sum((x - media) ** 2 for x in datos) / len(datos) if datos else 0

def obtener_desviacion_estandar(varianza):
    """Realizar función para obtener la desviación estandar de una lista de numeros"""
    return varianza ** 0.5

def main():
    """Definimos función principal"""
    if len(sys.argv) != 2:
        print("Usando: python ComputeStatistics.py fileWithData.txt")
        sys.exit(1)

    ruta_archivo = sys.argv[1]
    tiempo_inicio = time.time()

    numeros = leer_archivo(ruta_archivo)
    if not numeros:
        print("Numeros no validos")
        sys.exit(1)
    media = obtener_media(numeros)
    mediana = obtener_mediana(numeros)
    moda = obtener_moda(numeros)
    varianza = obtener_varianza(numeros, media)
    desviacion_estandar = obtener_desviacion_estandar(varianza)
    tiempo_ejecucion = time.time() - tiempo_inicio

    resultados = (
        f"Media: {media}\n"
        f"Mediana: {mediana}\n"
        f"Moda: {', '.join(map(str, moda)) if isinstance(moda, list) else moda}\n"
        f"Varianza: {varianza}\n"
        f"Desviación Estandar: {desviacion_estandar}\n"
        f"Tiempo de Ejecución: {tiempo_ejecucion:.4f} segundos"
    )

    print(resultados)
    with open("StatisticsResults.txt", "w", encoding="utf-8") as archivo_salida:
        archivo_salida.write(resultados)

if __name__ == "__main__":
    main()
