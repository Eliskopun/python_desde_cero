# Ejercicio 11
# Este programa simula el crecimiento de una cuenta de ahorros con un interés anual del 4%.
# Solicita al usuario la cantidad inicial depositada y calcula el balance final 
# después del primer, segundo y tercer año, mostrando cada cantidad redondeada a dos decimales.

inicial_usuario = float(input("Ingrese cantidad inicial depositada: "))
interes_anual = 0.04
primer_año = inicial_usuario * (1 + interes_anual)
segundo_año = primer_año * (1 + interes_anual)
tercer_año = segundo_año * (1 + interes_anual)

print(f"El balance del primer año: {primer_año:.2f}")
print(f"El balance del segundo año: {segundo_año:.2f}")
print(f"El balance del tercer año: {tercer_año:.2f}")