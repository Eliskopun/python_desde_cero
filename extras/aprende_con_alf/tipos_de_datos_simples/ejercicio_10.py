# Ejercicio 10
# Una juguetería vende payasos y muñecas por correo. 
# Cada payaso pesa 112 g y cada muñeca 75 g.
# Este programa solicita al usuario la cantidad de payasos y muñecas vendidas en el último pedido
# y calcula el peso total del paquete que será enviado.

nro_payaso_vendido = int(input("Ingrese la cantidad de payasos vendidas: "))
nro_munecas_vendido = int(input("Ingrese la cantidad de muñecas vendidas: "))

peso_total_paquete = (nro_payaso_vendido * 112) + (nro_munecas_vendido * 75)

print(f"El peso total es de: {peso_total_paquete}g")


