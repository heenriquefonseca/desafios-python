import random
import string

while True:
    try:
        tamanho = int(input("Qual o tamanho da senha? "))
        break
    except ValueError:
        print("Digite apenas números!")

maiuscula = input("Deseja letras MAIÚSCULAS? (s/n) ").lower() == 's'
minuscula = input("Deseja letras minúsculas? (s/n) ").lower() == 's'
numeros = input("Deseja números? (s/n) ").lower() == 's'
simbolos = input("Deseja símbolos? (s/n) ").lower() == 's'

caracteres = ''

if maiuscula:
    caracteres += string.ascii_uppercase
if minuscula:
   caracteres += string.ascii_lowercase
if numeros:
    caracteres += string.digits
if simbolos:
    caracteres += string.punctuation
if not caracteres:
    print('Você precisa escolher pelo menos um tipo de caracter!')
    exit()

senha = ''.join(random.choices(caracteres, k=tamanho))

print('Senha gerada:', senha)