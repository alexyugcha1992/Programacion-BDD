import random


player = input("Piedra, Papel o Tijera? :").lower()
my_random = ["Piedra", "papel", "tijera"]

my_random = random.choice(my_random)
print(my_random)

    #Logica del juego
if player == my_random:
        print("Empate")
elif player == "Piedra":
        if my_random == "Papel":
            print("Perdiste! ", my_random, " > ", player)
        else:
            print("Ganaste !", player, " < ", my_random)
elif player == "Papel":
        if my_random == "Tijera":
            print("Perdiste! ", my_random, " > ", player)
        else:
            print("Ganaste! ", player, " < ", my_random)
elif player == "Tijera":
        if my_random == "Piedra":
            print("Perdiste! ", my_random, " > ", player)
        else:
            print("Ganaste! ", player, " < ", my_random)



