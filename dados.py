import random
import sys

# Se define una funcion para que el jugador controle cuando empezar a jugar
def menu():
    eleccion = int(input("""
    ---

    Ingresa:
    
    * 1 para lanzar los dados
    * Otro numero para salir

    ---
    """))
    iniciar = 1

    if eleccion == iniciar:
        jugar()
    else:
        pass

# Se define la funcion con la logica del juego
def jugar():
    dado1 = random.randint(1, 6) # Genera un numero aleatorio entre 1 y 6 (ambos incluidos)
    dado2 = random.randint(1, 6) # Genera un numero aleatorio entre 1 y 6 (ambos incluidos)
    ganar = 4 # Detallo el valor ganador en una variable

    if dado1 + dado2 == ganar:
        print("Ganaste! La suma de los dados es: " , dado1 + dado2)
        menu()
    else:
        print("Perdiste! La suma de los dados es: " , dado1 + dado2)



menu()
print()