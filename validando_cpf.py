# Validando CPF

while True:
    cpf = str(input('\033[7mDigite um CPF:\033[m '))
    novo_cpf = cpf[:-2]   # Elimina os dois últimos dígitos do CPF

    reverso = 10   # Contador reverso
    total = 0
    for index in range(19):
        if index > 8:   # Primeiro índice vai de 0 a 9
            index -= 9   # São os 9 primeiros dígitos do CPF

        total += int(novo_cpf[index]) * reverso   # Valor total da multiplicação

        reverso -= 1   # Decréscimo  do contador reverso
        if reverso < 2:
            reverso = 11
            digito = 11 - (total % 11)

            if digito > 9:   # Se o dígito for maior que 9 o valor é 0
                digito = 0
            total = 0   # zera o total
            novo_cpf += str(digito)   # concatena o dígito gerado no novo cpf

    sequencia = novo_cpf == str(novo_cpf[0] * len(cpf))   # Evita sequências tipo 11111111111, 00000000000
    if cpf == novo_cpf and not sequencia:
        print('\033[36mCPF válido!\033[m')
    else:
        print('\033[31mCPF inválido!\033[m')
    print('')
