# Ejercicio 8
# Este programa solicita al usuario dos números enteros y muestra en pantalla 
# el resultado de la división entera en el formato: 
# "<n> entre <m> da un cociente <c> y un resto <r>",
# donde <n> y <m> son los números ingresados por el usuario,
# y <c> y <r> representan el cociente y el resto de la división entera respectivamente.

n = int(input("Ingrese un numero entero: "))
m = int(input("Ingrese otro numero entero: "))

c = n // m
r = n % m

print(f"{n} entre {m} da un cociente {c} y un resto {r}")