player = input("Piedra, Papel o Tijera? :").lower()
computer = "Piedra".lower()

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


