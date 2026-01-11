#Valiadacion de nombre
'''while True:
    nombreGladiador = input("Ingrese el nombre del gladiador: ")
    if nombreGladiador.isalpha():
        break
    else:
        print("\nPor favor, ingrese un nombre valido")
        nombreGladiador = input("Ingrese el nombre del gladiador: ")'''

nombreGladiador = input("Indique el nombre del gladiador: ").strip()
while not nombreGladiador.isalpha():
    print("Ingreso un nombre invalido. Solo se permiten letras")
    nombreGladiador = input("Indique el nombre del gladiador: ").strip()

nombreGladiador = nombreGladiador.capitalize()

#Inicializacion de estadisticas
vidaGladiador = 100
vidaEnemigo = 100
pocionesVida = 3
dañoBaseGladiador = 15
dañoBaseEnemigo = 12
turnoGladiador = True

#Inicio de juego
while vidaGladiador > 0 and vidaEnemigo > 0:
    if turnoGladiador:
        print(f"Vida gladiador : {vidaGladiador} ")
        print(f"Vida enemigo: {vidaEnemigo}")
        print(f"Pociones: {pocionesVida}")

        while True:
            opcion = input('''
                        Ingrese una opción:
                        1. Ataque Pesado
                        2. Ráfaga Veloz
                        3. Curar 
                        ''').strip()
            while not opcion.isdigit():
                print("Error, opción invalida.")
                opcion = input('''
                        Ingrese una opción:
                        1. Ataque Pesado
                        2. Ráfaga Veloz
                        3. Curar 
                        ''').strip()
                
            opcion = int(opcion)

            match opcion:
                case 1:
                    dañoFinal = 0
                    if vidaEnemigo <= 20:
                        dañoFinal = dañoBaseGladiador * 1.5
                    else:
                        dañoFinal = dañoBaseGladiador
                    vidaEnemigo = vidaEnemigo - dañoFinal
                    print(f"¡Atacaste al enemigo por {dañoFinal} puntos de daño!")
                    turnoGladiador = False
                    break
                case 2:
                    for i in range(3):
                        vidaEnemigo -= 5
                        print(">Golpe conectado por 5 de daño")
                    turnoGladiador = False
                    break
                case 3:
                    if pocionesVida > 0:
                        vidaGladiador += 30
                        pocionesVida -= 1
                    else:
                        print("¡No quedan pociones!")
                    turnoGladiador = False
                    break
                case _:
                    print("El número ingresado no es valido.")
    else:
        vidaGladiador = vidaGladiador - dañoBaseEnemigo
        print(f"¡El enemigo te atacó {dañoBaseEnemigo} por puntos de daño!")
        turnoGladiador = True

if vidaGladiador > 0:
    print(f"¡VICTORIA! [{nombreGladiador}] ha ganado la batalla.")
else:
    print("DERROTA. Has caido en combate.")