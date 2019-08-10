# Exercício 1
# Crie um arquivo .py que dado os números de 0 a 1000. 
# Some todos os impares. 
# Neste exercício tente usar a abordagem de list compreension(Olhe o conteudo auxiliar).

numbers = range(1000)
result = 0

for single_number in numbers:
    if not single_number % 2 == 0:
        result += single_number
print(result)

# using List Comprehensions
result = sum([single_number for single_number in numbers if not single_number % 2 == 0])
print(result)
