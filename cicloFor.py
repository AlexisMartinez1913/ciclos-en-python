"""
Se cuenta con la siguiente información:
Las edades de 5 estudiantes del turno mañana.
Las edades de 6 estudiantes del turno tarde.
Las edades de 11 estudiantes del turno noche.
Las edades de cada estudiante deben ingresarse por teclado.
a) Obtener el promedio de las edades de cada turno (tres promedios)
b) Imprimir dichos promedios (promedio de cada turno)
c) Mostrar por pantalla un mensaje que indique cual de los tres turnos tiene un promedio de edades mayor.
"""



turnoMañana = 0
turnoTarde = 0
turnoNoche = 0
promedioMañana = 0
promedioTarde = 0
promedioNoche = 0
print("TURNO MAÑANA")
for x in range(1,6):
    edadesM = int(input("Ingrese la edad del estudiante: "))
    turnoMañana = turnoMañana + edadesM
print()
print("TURNO TARDE: ")
for x in range(1,7):
    edadesT = int(input("Ingrese la edad del estudiante: "))
    turnoTarde = turnoTarde + edadesT
print()
print("TURNO NOCHE")
for x in range(1,12):
    edadesN = int(input("Ingrese la edad del estudiante: "))
    turnoNoche = turnoNoche + edadesN
promedioMañana = (turnoMañana/5)
promedioTarde = (turnoTarde/6)
promedioNoche = (turnoNoche/11)

print("El promedio de edades del turno de la mañana es igual a: ", promedioMañana)
print("El promedio de edades del turno de la tarde es igual a: ", promedioTarde)
print("El promedio de edades del turno de la noche es igual a: ", promedioNoche)

if promedioMañana > promedioTarde and promedioMañana > promedioNoche:
    print("El turno de la mañana tiene un promedio mayor")
elif promedioTarde > promedioMañana and promedioTarde > promedioNoche:
    print("el turno de la tarde tiene un promedio mayor")
else:
    print("el turno de la noche tiene un promedio mayor")


