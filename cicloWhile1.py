"""
Se ingresan un conjunto de n alturas de personas por teclado. Mostrar la altura promedio de las personas
"""
n = int(input("Ingrese la cantidad de personas: "))
suma = 0
x = 1
while x <=n:
    alturas = float(input("Ingrese la altura de la persona  : "))
    suma = suma + alturas
    x = x+1
print()
promedio = (suma/n)
print("El promedio de alturas es igual a: ", promedio)

