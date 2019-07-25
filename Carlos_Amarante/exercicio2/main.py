def fizzbuzz(number):
    if (number % 3 == 0):
        print('fizz', end='')
    if (number % 5 == 0):
        print('buzz')

print('Primeiro teste:')
fizzbuzz(15)
print('Segundo teste:')
fizzbuzz(9)
print('\nTerceiro teste:')
fizzbuzz(5)

# Usei o end no final do print para evitar colocar mais um if com && , pois se os dois forem
# divisíveis, um irá ser escrito junto ao outro