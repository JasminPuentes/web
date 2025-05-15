#Escribe esta linea de codigo
print("binvenidos al entrenamiento con python, vamos a disfrutar esta sesion")

"""
    Descuento en uana compra:
    Si compras mas de $1000, optienes un descuento del 20% 
    pide el onto de la compra y muestra el monto final
"""

#pedir datos por teclado al usuario int (entero) float (decimal) str (cadenas de caracteres) bool (boleano)

compra = float(input("Digita el valor de tu compra: "))

#si compras mas de $1000, optienes un descuento del 20%.
#Siempre que la salida tenga mas de un camino de resolución, debo implementar condicionales.
#Operadores combinados.
#Operadores de asignacion =, operadores aritmeticos +, -, *, /, operadores logicos and y, or o, not no
# #operadores de comparacion ==, !=, >, <, >=, <=,  

if compra > 1000: 
    descuento = compra * 0.20
    total = compra - descuento
print(f"El descuento es {descuento}, el costo total de tu compra es: ", total)



# Ejemplo basico de uso de print
mensaje = "Hola, mundo!"
print(mensaje)

# Formateo de cadenas
nombre = "Ana"
edad = 30
print(f"Mi nombre es {nombre} y tengo {edad} años.")

# Cambiando el carcter al final de la salida
print("Hola" , end="")
print("mundo!")

# Esécificando un separador diferente
nombre ="juan"
edad = 25
print( nombre, edad, sep="-")

# Ejemplo de declaración y asignación de variables
nombre = "John" # Una variable de cadena
altura = 1.75 # Una variable de punto flotante
es_estudiante = True # Una variable booleana

# Asignacion de valores en la declaración
ciudad = "Nueva York"
poblacióin = 8500000


# Reasignación de valores en la declaración
ciudad = "Los angeles"
poblacion = 4000000

# Convenciones de nombres
nombre_completo = "Jane Done" 
temperatura_actual = 23.5

# Tipos de variables dinámicos
variable_dinamica = 10
print(variable_dinamica) # Salida: 10

variable_dinamica = "Hola"
print(variable_dinamica) # Salida: Hola

# Enteros
entero_positivo = 10
entero_negativo = -5

# Flotantes
flotante_1 = 3.14
flotante_2 = -0.5

# Operaciones con enteros y flotantes
resultado_suma = entero_positivo + flotante_1
resultado_multiplicacion = entero_negativo * flotante_2

# Impresión de resultados
print(resultado_suma) 
print(resultado_multiplicacion)

#cadenas
cadena_simple = 'Hola, mundo!'
cadena_doble = "Phython es divertido"

# Concatenación de cadenas
saludo_completo = cadena_simple + " " + cadena_doble
print(saludo_completo) 


