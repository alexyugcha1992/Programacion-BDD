
player = input("Piedra, Papel o Tijera? :")
computer = "Piedra"

    #Logica del juego
if player == computer:
        print("Empate")
elif player == "Piedra":
        if computer == "Papel":
            print("Perdiste! ", computer, " > ", player)
        else:
            print("Ganaste !", player, " < ", computer)
elif player == "Papel":
        if computer == "Tijera":
            print("Perdiste! ", computer, " > ", player)
        else:
            print("Ganaste! ", player, " < ", computer)
elif player == "Tijera":
        if computer == "Piedra":
            print("Perdiste! ", computer, " > ", player)
        else:
            print("Ganaste! ", player, " < ", computer)
else:
        print("Error - Opción no valida, Intenta escribir las opciones como se las ve.")
