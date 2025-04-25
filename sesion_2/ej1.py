# Escribe un Programa de califaciones (0-10) a A-F
# Rangos: A (9-10) B (7-8) C (5-6) D (3-4) F (0-2) 

calificacion = float(input("Ingrese su calificacion (0-10): "))

if calificacion >= 9 and calificacion <=10: 
    print("La Calificacion es: A")
elif calificacion >=7 and calificacion <=8:
    print("La Calificacion es: B")
elif calificacion >=5 and calificacion <=6:
    print("La Calificacion es: C")
elif calificacion >=3 and calificacion <=4:
    print("La Calificacion es: D")
elif calificacion >=0 and calificacion <=2:
    print("La Calificacion es: F")
else: print("Error. La calificacion ingresada no es valida.")