# Calculo de Interes Compuesto

cap_in = int(input("Ingrese capital inicial: "))
tasa = int(input("Ingrese la tasa de interes actual (Porcentaje): "))
years = int(input("Ingrese la cantidad de años: "))

tasadec = tasa/100
capita = (1+tasadec)**years
mont_fin = capita*cap_in

inter_ganado = mont_fin - cap_in

print("="*20)
print(f"""Capital Inicial: {cap_in}
Tasa: {tasa}
Años {years}
Monto Final: {mont_fin:.0f}
Interes Ganado {inter_ganado:.0f}""")
print("="*20)