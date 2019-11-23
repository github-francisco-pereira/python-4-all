
#Crie um arquivo .py que contenha uma função que receba um número inteiro
#e se o número for divisivel por 3 você exibe fizz no console. 
# Se o número for divisivel por 5 você exibe buzz, caso seja por 5 e 3 você exibe fizzbuzz.

def divisao(numero):
    num = int(numero)
    if num % 3 == 0:
        if num % 5 == 0:
                print("fizzbuzz")
        else: print ("fizz")
    elif num % 5 == 0:
        print("buzz")
    else: return False

divisao(15)
divisao(6)
divisao(5)
divisao(4)