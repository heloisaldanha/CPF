# Gerando CPF
from random import randint

numero = str(randint(100000000, 999999999))


novo_cpf = numero

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

print(novo_cpf)
