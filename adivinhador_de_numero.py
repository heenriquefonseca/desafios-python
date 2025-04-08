#Desafio Adivinhador de Números.

import random

numero_secreto = random.randint(1, 100)

while True:
    palpite = int(input("Digite um número: "))

    if palpite == numero_secreto:
        print("Parabéns! Você acertou!")
        break
    elif palpite > numero_secreto:
        print("Muito alto!")
    else:
        print("Muito baixo!")

print("O número era:", numero_secreto)

