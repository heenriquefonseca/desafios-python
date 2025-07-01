print('Digite seu CPF para verificar se ele é válido.')
cpf = input().replace('.', '').replace( '-', '')

# Verificando o primeiro dígito
nove_digitos = cpf[:9]
contador_regressivo_1 = 10

resultado_digito_1 = 0
for digito_1 in nove_digitos:
    resultado_digito_1 += int(digito_1) * contador_regressivo_1 
    contador_regressivo_1 -= 1
digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

dez_digitos = cpf[:10]
contador_regressivo_2 = 11

# Verificando o segundo dígito
resultado_digito_2 = 0
for digito_2 in dez_digitos:
    resultado_digito_2 += int(digito_2) * contador_regressivo_2
    contador_regressivo_2 -= 1
digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

# Verificando se o CPF é válido
cpf_calculado = nove_digitos + str(digito_1) + str(digito_2)

if cpf == cpf_calculado:
    print('VÁLIDO.')
else:
    print('INVÁLIDO.')
