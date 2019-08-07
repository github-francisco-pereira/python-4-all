# 3 - Dificuldade Média - Retornar apelido dos usuarios
# Crie um arquivo .py que tenha um dicionario com 10 usuários.
# O dicionário deve conter as chaves: `nome`, `apelido` e `data_nascimento`.
# Crie uma função que retorne somente uma lista com os apelidos.

# cd aula_2/anahamud/
# python3 exercicio3.py

usuarios = {
    "usuario0": {
        "nome": "Ana", "apelido": "Ná", "data_nascimento": "19900101"
    },
    "usuario1": {
        "nome": "Bruna", "apelido": "Bru", "data_nascimento": "19900201"
    },
    "usuario2": {
        "nome": "Camila", "apelido": "Ca", "data_nascimento": "19900301"
    },
    "usuario3": {
        "nome": "Dalila", "apelido": "Da", "data_nascimento": "19900401"
    },
    "usuario4": {
        "nome": "Eliane", "apelido": "Li", "data_nascimento": "19900501"
    },
    "usuario5": {
        "nome": "Fabiana", "apelido": "Fab", "data_nascimento": "19900601"
    },
    "usuario6": {
        "nome": "Gisele", "apelido": "Gi", "data_nascimento": "19900701"
    },
    "usuario7": {
        "nome": "Hannah", "apelido": "Nah", "data_nascimento": "19900801"
    },
    "usuario8": {
        "nome": "Isabel", "apelido": "Bel", "data_nascimento": "19900901"
    },
    "usuario9": {
        "nome": "Juliana", "apelido": "Ju", "data_nascimento": "19901001"
    },
}


def main(usuarios):
    return [usuarios[usuario]["apelido"] for usuario in usuarios]

print("Apelidos encontrados: ", main(usuarios))
