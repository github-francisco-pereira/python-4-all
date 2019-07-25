num1 = int(input("Digite o numero inicial:"))

num2 = int(input("Digite o numero final:"))

list = [numero for numero in range(num1, num2)]

for numero in list:
    if numero % 5 == 0 and numero % 3 == 0:
        print ('fizz-buzz')
    elif numero % 3 == 0:
        print ('fizz')
    elif numero % 5 == 0:
        print ('buzz')
    else:
        print (numero)
