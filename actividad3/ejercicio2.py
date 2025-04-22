# Control de Inventario de un Producto
cantinic = int(input("Ingresar la cantidad inicial: "))
cantrec = int(input("Ingresar cantidad de productos recibidos: "))
cantven = int(input("Ingresar la cantidad de productos vendidos: "))

suma = cantinic + cantrec
inventario_ac = suma - cantven

print("="*20)
print(f"Inventario Inicial: {cantinic:.0f}")
print(f"Productos Vendidos {cantven:.0f} y Recibidos: {cantrec:.0f}")
print(f"Inventario Actual: {inventario_ac:.0f}")
print("="*20)

