# Ejercicio 12
# Una panadería vende barras de pan a 3.49€ cada una, 
# pero las que no son del día tienen un 60% de descuento.
# Este programa solicita al usuario la cantidad de barras de pan vendidas que no son del día,
# luego muestra el precio habitual, el descuento aplicado y el coste final total.

nro_barras_vendidas = float(input("Ingrese la cantidad de barras de pan vendidas que no son del día: "))
print(f"El precio habitual: {nro_barras_vendidas * 3.49:.2f}€ \nDescuesto: {nro_barras_vendidas * 3.49 * 0.6:.2f}€ \nCoste final: {nro_barras_vendidas * 3.49 * 0.4:.2f}€")