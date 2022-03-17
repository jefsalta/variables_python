# Tipos de variables [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con números
'''
Enunciado:
Realice un calculadora, se ingresará por línea de comando dos
números reales y se deberá calcular todas las operaciones entre ellos:
A) Suma
B) Resta
C) Multiplicación
D) División
E) Exponente/Potencia

- Para todos los casos se debe imprimir en pantalla el resultado aclarando
  la operación realizada en cada caso y con que números
  se ha realizado la operación
  ej: La suma entre 4.2 y 6.5 es 10.7
'''

print('¡Nuestra primera calculadora!')
# Empezar aquí la resolución del ejercicio
print('''
         1) Suma
         2) Resta
         3) Multiplicación
         4) División
         5) Exponente/Potencia''')
print("Selecciones una opción: ")
opcion= int(str(input()))
if opcion == 1:
    numero1= int(str(input("Ingrese un numero: ")))
    numero2= int(str(input("Ingrese un numero: ")))
    print("La suma entre",numero1,"y",numero2,"es",numero1+numero2)
elif opcion == 2:
     numero1= int(str(input("Ingrese un numero: ")))
     numero2= int(str(input("Ingrese un numero: ")))
     print("La resta entre",numero1,"y",numero2,"es",numero1 - numero2)
elif opcion == 3:
      numero1= int(str(input("Ingrese un numero: ")))
      numero2= int(str(input("Ingrese un numero: ")))
      print("La multiplicacion entre",numero1,"y",numero2,"es",numero1 * numero2)
elif opcion == 4:
      numero1= int(str(input("Ingrese un numero: ")))
      numero2= int(str(input("Ingrese un numero: ")))
      print("La division entre",numero1,"y",numero2,"es",numero1 / numero2)
else:
      numero1= int(str(input("Ingrese un numero: ")))
      numero2= int(str(input("Ingrese un numero: ")))
      print("La potencia entre",numero1,"y",numero2,"es",numero1 ** numero2)