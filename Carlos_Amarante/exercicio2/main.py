def fizzbuzz(number):
    if (number % 3 == 0):
        print('fizz')
    if (number % 5 == 0):
        print('buzz')

print('Primeiro teste:')
fizzbuzz(15)
print('Segundo teste:')
fizzbuzz(9)
print('Terceiro teste:')
fizzbuzz(5)

# minha ideia era tentar poupar que ele faça duas verificações iguais do resto 3 e resto 5
# não usar number % 3 == 0 && number % 5 == 0 (pois ele ja viu antes) , mas não consegui arrumar
# um jeito que ele printasse fizzbuzz junto. Ele ta printando os dois separadamente