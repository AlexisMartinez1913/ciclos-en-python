"""
Desarrollar un programa que permita cargar n números enteros y luego nos informe cuántos valores fueron pares y cuántos impares.
Emplear el operador “%” en la condición de la estructura condicional (este operador retorna el resto de la división de dos valores, por ejemplo 11%2 retorna un 1):
"""

n = int(input("Cantidad de numeros a procesar:  "))
pares = 0
impares = 0
x = 1
while x <=n:
    num = int(input("Digite un número entero: "))
    if num %2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1
    x = x+1

print("Cantidad de numeros pares que digitó: ")
print(pares)
print("Cantidad de numeros impares que digitó: ")
print(impares)

