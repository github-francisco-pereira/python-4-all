lista_do_chico = [1,2,3] #exemplo lista
a =3

for item in lista_do_chico:
    print(item)
    if a == item:
        break #ma pratica


#for é para iterar uma lista
#while é para iterar até que uma condição seja atendida


def get_person(person):
    return {'name': person['nome'], 'age': person['idade']}


for item in lista_do_chico:
    print(item) 

a=1
saida=False
while not saida:
    a+= 1

# list compreenhension
soma=0
lista_nova = [1,2,3,4,5,6]
for numero in lista_nova:
    if numero % 2 == 0:
        soma += numero

numeros = sum([numero for numero in lista_nova if numero % 2 == 0])

pessoa1 = {
    'nome': 'Chico',
    'idade': 18
}

pessoa2 = {
    'nome': 'Luiz',
    'idade': 15
}
lista = [pessoa1, pessoa2]
nome_pessoas = [get_person(pessoa) for pessoa in lista]
nome_pessoas_2 = []

for pessoa in lista:
    nome_pessoas_2.append(get_person(pessoa))


lista = []
lista.append('oi')
lista.append(1)

dicionario = {
    'key': 1
}


def funcao_errada(item):
    if item > 2:
        return 'legal'

#https://pt.wikipedia.org/wiki/Duck_typing
# SOLID - artigo
# Orientacao a objetos - artigo
#callable()

#kwargs - documentacao
#sobrecarga de metodos
#boto3 gerencia comunicacao com a aws
a = {
    'param': 1,
    'param_2': 2
}



def chamada_1(**kwargs):
    print(a)

chamada_1(**a)

chamada_1(param=1, param_2=2)

def chamando_com_kwargs(**kwargs):
    kwargs['param1']
    kwargs['param2']


def chamando_funcao(funcao):
    messagem_fila = pegar_mensagem()
    funcao(messagem_fila)


chamando_funcao(funcao_errada)

a_b =1
if not a_b > 1: #negacao
    print('teste')

if not a_b > 1 and a_b != 3: # and
    print('oi com and')

if not a_b > 1 or a_b != 3:#exemplo com or
    print('oi com or')