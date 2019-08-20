"""
Exercício 2
Crie um arquivo .py que receba uma lista com 10 números.
Crie uma função que retorne o primeiro número primo encontrado nessa lista.
Lembre se de usar a melhor estrutura de repetição para isso.
"""


def find_first_prime(numbers):
    if not numbers:
        return 'Empty list'

    i = 0
    while i < len(numbers):
        if is_prime(numbers[i]):
            return numbers[i]
        i += 1
    return 'Not found prime'


def is_prime(number):
    number = int(number)
    base_prime = [2, 3, 5, 7]

    if number < base_prime[0]:
        return False

    i = 0
    while i < len(base_prime):
        if number > base_prime[i] and number % base_prime[i] == 0:
            return False
        i += 1
    return True

numbers = [6, 7, 8, 9, 10, 11, 12, 22, 33, 35]
print(find_first_prime(numbers))
