# Consumo de Combustible

distanc_km = int(input("Ingrese la distancia recorrida en Km: "))
lits_cons = int(input("Ingrese la cantidad de litros consumidos: "))

rendimiento = distanc_km/lits_cons
gasto = 48.97 * lits_cons

print("="*20)
print(f"""Distancia: {distanc_km}
Litros: {lits_cons}
Precio por Litro: 48.97
Rendimiento del Vehiculo: {rendimiento}
Gasto Total en Combustible {gasto}""")
print("="*20)