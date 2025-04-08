 # Calculadora
 
while True:
    number_1 = input('Digite um número: ')
    number_2 = input('Digite um segundo número: ')

    calculo = input('Escolha uma operação usando +, -, * ou /: ')

    numero_valido = None

    try:
        num_1_float = float(number_1)
        num_2_float = float(number_2)
        numero_valido = True
    except:
        numero_valido = None

    if numero_valido is None:
        print('Um ou ambos os números são inválidos!')
        continue

    if calculo not in '+-*/':
        print('Operador inválido!')
        continue

    if len(calculo) > 1:
        print('Digite apenas um operador!')
    
    if numero_valido is True:
        if calculo == '+':
            print('A soma entre',  num_1_float, 'e',  num_2_float, 'é igual',  num_1_float +  num_2_float)

        elif calculo == '-':
            print('A subtração entre',  num_1_float, 'e',  num_2_float, 'é igual',  num_1_float -  num_2_float)
    
        elif calculo == '*':
            print('A multiplicação entre',  num_1_float, 'e',  num_2_float, 'é igual',  num_1_float *  num_2_float)

        elif calculo == '/':
            print('A divisão entre',  num_1_float, 'e',  num_2_float, 'é igual',  num_1_float /  num_2_float)

    sair = input('Você deseja sair do programa? [s]im: ').lower().startswith('s')

    if sair is True:
        break

    
    