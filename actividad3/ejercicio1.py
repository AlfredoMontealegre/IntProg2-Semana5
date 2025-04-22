calificacion1 = int(input("Ingrese la calificacion 1: "))
calificacion2 = int(input("Ingrese la calificacion 2: "))
calificacion3 = int(input("Ingrese la calificacion 3: "))

suma = calificacion1+calificacion2+calificacion3
promedio = suma/3

#El ":>3" hace que se ordene dependiendo la longitud y valores, como asi 1 unidad, 2 decena, 3 centena. etc.

print("="*20)
print(f"""Calificacion 1: {calificacion1:>3}
Calificacion 2: {calificacion2:>3}
Calificacion 3: {calificacion3:>3} 
{"Promedio:":<15} {promedio:>3.0f} """)
print("="*20)

# 0f = Sin Decimales (El 0 es la cantidad supongo de decimales mostrados)