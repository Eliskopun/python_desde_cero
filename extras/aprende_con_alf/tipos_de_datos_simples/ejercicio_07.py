# Ejercicio 7
# Este programa solicita al usuario su peso (en kg) y estatura (en metros),
# calcula el índice de masa corporal (IMC) y lo almacena en una variable.
# Finalmente, muestra en pantalla el resultado con dos decimales.

kg_usuario = float(input("Introduzca su peso en kilogramos: "))
estatura_usuario = float(input("Introduzca su estatura en metros: "))

indice_masa_corporal = kg_usuario / estatura_usuario ** 2

print(f"Su indice de masa corporal es de: {indice_masa_corporal:.2f}")

