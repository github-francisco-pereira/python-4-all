# 1 - Dificuldade Fácil - Somar todos os números impares
# Crie um arquivo .py que dado os números de 0 a 1000. Some todos os impares.
# Neste exercício tente usar a abordagem de list compreension
# (Olhe o conteudo auxiliar).

# cd aula_2/anahamud/
# python3 exercicio1.py

soma = sum([odd_number for odd_number in range(1000) if odd_number % 2 != 0])
print(soma)
