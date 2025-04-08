#Desafio Conversor de Celsius para Farenheit.

def c_para_f (celsius):
    return (celsius * 9/5) + 32

def f_para_c (farenheit):
    return (farenheit - 32) * 5/9

temperatura = float(input('Qual a temperatura?'))
unidade = input('Digite a unidade (C para Celsius e F para Farenheit): ').upper()

if unidade == 'C' :
    resultado = c_para_f(temperatura)
    print(f"{temperatura} graus Celsius é igual a {resultado: .2f} graus Farenheit")
elif unidade == 'F':
    resultado = f_para_c(temperatura)
    print(f"{temperatura} graus Farenheit é igual a {resultado: .2f} graus Celsius")
else:
    print("Unidade inválida. Escolha apenas C e F.")