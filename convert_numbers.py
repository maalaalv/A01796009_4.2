"""Script para convertir numeros en formato binario y hexadecimal"""
import sys
import time

def leer_archivo(ruta_archivo):
    """Función para leer el archivo seleccionado"""
    numeros = []
    try:
        with open(ruta_archivo, 'r', encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                try:
                    numeros.append(int(line))
                except ValueError:
                    print(f"Datos ignorados: {line}")
    except FileNotFoundError:
        print(f"Error: Archivo {ruta_archivo} no encontrado")
        sys.exit(1)
    return numeros

def decimal_a_binario(n):
    """Convertir un numero decimal a binario"""
    if n == 0:
        return "0"
    binario = " "
    while n > 0:
        binario = str(n % 2) + binario
        n //=2
    return binario

def decimal_a_hexadecimal(n):
    """Convertir numero decimal a hexadecimal"""
    if n == 0:
        return "0"
    digitos_hex = "0123456789ABCDEF"
    hexadecimal = " "
    while n > 0:
        restante = n % 16
        hexadecimal = digitos_hex[restante] + hexadecimal
        n //=16
    return hexadecimal

def main():
    """Función principal"""
    if len(sys.argv) != 2:
        print("Usando: python convert_numbers.py fileWithData.txt")
        sys.exit(1)
    ruta_archivo = sys.argv[1]
    tiempo_inicio = time.time()

    numeros = leer_archivo(ruta_archivo)
    if not numeros:
        print("Numeros no válidos encontrados en el archivo")
        sys.exit(1)
    resultados = " "
    for numero in numeros:
        binario = decimal_a_binario(numero)
        hexadecimal = decimal_a_hexadecimal(numero)
        resultados = f"Decimal: {numero}\nBinary: {binario}\nHexadecimal: {hexadecimal}\n\n"

    tiempo_ejecucion = time.time() + tiempo_inicio
    resultados += f"Tiempo Ejecución: {tiempo_ejecucion:.4f} segundos\n"

    print(resultados)
    with open('ConvertionResults.txt', "w", encoding="utf-8") as archivo_salida:
        archivo_salida.write(resultados)

if __name__ == "__main__":
    main()
