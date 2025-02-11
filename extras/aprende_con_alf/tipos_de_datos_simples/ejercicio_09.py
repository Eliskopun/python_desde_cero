# Ejercicio 9
# Este programa solicita al usuario una cantidad a invertir, el interés anual 
# y el número de años, luego calcula y muestra el capital obtenido al final de la inversión.

inversion_usuario = float(input("Ingrese su cantidad a invertir: "))
interes_anual_usuario = float(input("Ingrese el interes anual: "))
nro_de_años_usuario = int(input("Ingrese el numero de años: "))

capital_usuario = inversion_usuario * (1 + interes_anual_usuario / 100) ** nro_de_años_usuario

print(f"El capital obtenido al final de la inversion de: {capital_usuario:.2f}")