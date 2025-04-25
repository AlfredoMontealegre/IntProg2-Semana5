# Programa de Sueldo, Cacule sueldo, bono y porcentajes implicados.

print("="*20)
sueldo = int(input("Ingrese su sueldo: "))

if sueldo > 3000:
    bono = 0.10
elif sueldo > 1500 <= 3000:
    bono = 0.05
elif sueldo >= 1500:
 bono = 0

bonoapl = sueldo * bono
sueldof = sueldo + bonoapl

print(f"""El Sueldo Final es: {sueldof}
Bono Aplicado = {bonoapl}""")
