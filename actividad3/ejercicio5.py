# Consumo de Agua x Persona
lts_consm_vivienda = int(input("Ingresar cant. Litros consumidos en el mes: "))
cant_personas = int(input("Ingresar cant. de personas que habitan: "))

consm_mensual = lts_consm_vivienda/cant_personas
consumo_diario = consm_mensual/30

print("="*20)
print(f"""Consumo Mensual: {lts_consm_vivienda}
Cantidad de Personas: {cant_personas}
Consumo Mensual Por Persona: {consm_mensual:.1f}
Consumo Diario Por Persona: {consumo_diario:.1f}""")
print("="*20)