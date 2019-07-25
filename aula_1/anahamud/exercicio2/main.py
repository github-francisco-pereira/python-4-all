# virtualenv venv
# source venv/bin/activate
# python main.py
# deactivate

import sys

def main():
    numero = int(sys.argv[1])
    print("numero recebido: " , numero)
    resultado = ""
    if(numero % 3 == 0):
        resultado += "fizz"
    if (numero % 5 == 0):
        resultado += "buzz"
    print(resultado)

main()