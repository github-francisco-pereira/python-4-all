# 2 - Dificuldade Fácil - Achar um número primo
# Crie um arquivo .py que receba uma lista com 10 números.
# Crie uma função que retorne o primeiro número primo encontrado nessa lista.
# Lembre se de usar a melhor estrutura de repetição para isso.

# cd aula_2/anahamud/
# python3 exercicio2.py 0 1 2 3 4 5 6 7 8 9 10

import sys


def is_prime_number(number):
    number = int(number)

    if number <= 1:
        return False

    if number > 2 and number % 2 == 0:
        return False

    if number > 3 and number % 3 == 0:
        return False

    if number > 5 and number % 5 == 0:
        return False

    if number > 7 and number % 7 == 0:
        return False

    return True


def main():
    i = 1
    while i < len(sys.argv) and i <= 10 and not is_prime_number(sys.argv[i]):
        i += 1

    return int(sys.argv[i])

print("Primeiro numero primo encontrado: ", main())
