# Programa de numeros (1 = Lunes, 2 = Martes, etc)
# Rango = 1-7

print("="*20)
dia = int(input("Ingrese un numero de dia en la semana (1-7): "))

if dia == 1:
    print("Lunes: Dia de trabajo")
elif dia == 2:
    print("Martes: Segundo Dia")
elif dia == 3:
    print("Miercoles: Tercer Dia")
elif dia == 4:
    print("Jueves: El Cuarto Dia")
elif dia == 5:
    print("Viernes: El favorito de todos")
elif dia == 6:
    print("Sabado: Fin de Semana")
elif dia == 7:
    print ("Domingo: Dia de Descanso")
else: print("Numero Invalido, (1-7)")

print(f"Numero correspondiente a: {dia:.0f}")