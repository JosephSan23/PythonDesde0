###
# Forma de pedir informacion
###

print("Hola, ¿Como te llamas?\n")
nombre = input()

print(f"Hola {nombre}, encantado de conocerte")

age = input("¿Cuantos años tienes?\n")
age = int(age)
print(f"Tienes {age} años")

print("Obtener multiples valores a la vez")
country, city = input("¿En que pais y ciudad vives?\n").split()

print(f"Vives en {country}, en la ciudad de {city}")
