# Exercício 2
# Crie um arquivo .py que receba uma lista com 10 números. 
# Crie uma função que retorne o primeiro número primo encontrado nessa lista.
# Lembre se de usar a melhor estrutura de repetição para isso.

def find_first_prime(numbers):
    i=0
    while i <= len(numbers) and not is_prime(numbers[i]):
        i+=1
    return numbers[i]

def is_prime(number):
    number = int(number)

    if number < 2:
        return False

    if number > 2 and number % 2 == 0:
        return False

    if number > 5 and number % 5 == 0:
        return False

    if number > 7 and number % 7 == 0:
        return False

    return True

numbers = [6,7,8,9]
print(find_first_prime(numbers))
