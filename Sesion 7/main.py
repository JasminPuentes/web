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

#Formateo de cadenas
nombre = "Ana"
edad = 30
print(f"Mi nombre es {nombre} y tengo {edad} años.")

#Cambiando el carcter al final de la salida
print("Hola" , end="")
print("mundo!")

#Esécifi