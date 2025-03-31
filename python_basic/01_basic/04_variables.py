###
# Variables en python
# Python es un lenguaje de tipado dinamico y de tipado fuerte
###

# Asignar una variable

age = 32
print(age)

age = 39
print(age)

# Tipado dinamico: el tipo de dato se determina en tiempo de jecucion
# No tienes que declararlo explicitamente
name = "joseph"
print(type(name))

name = 32
print(type(name))

# Tipado fuerte: python no realiza conversiones de tipo automaticamente

# f-string (literal de cadena de formato)
# desde la version Python 3.6
print(f"Hola {name}, tengo {age} años")

# Forma no recomendada de asignar variables
name, age, city = "joe", 32, "bogota"

# Convenciones de nombres de variables
my_variable_name = "siuuuuuu" # snake_case

## Constante un valor que no debe cambiar,
MI_CONSTANTE = 3.14 # UPPER_CASE -> constantes



