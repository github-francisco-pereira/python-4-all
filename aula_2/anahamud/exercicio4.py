# 4 - Dificuldade Eita pipoco - Retornar usuários maiores de idade
# Crie um arquivo .py que tenha um dicionario com 100 usuários.
# O dicionário deve conter as chaves: `nome`, `apelido` e `data_nascimento`.
# Crie uma função que retorne somente usuários maiores de idade.

# cd aula_2/anahamud/
# python3 exercicio4.py

import datetime
from dateutil.relativedelta import relativedelta


def get_usuarios():
    usuarios = {}

    i = 0
    while i < 100:
        nome = "usuario" + str(i)
        usuario = {}.fromkeys(["nome", "apelido", "data_nascimento"], nome)

        usuario["data_nascimento"] = str(2019 - i) + "-08-06"

        usuarios[i] = usuario

        i += 1

    return usuarios


def is_adult(data_nascimento):
    now = datetime.date.today()

    date = data_nascimento.split("-")
    date = datetime.date(int(date[0]), int(date[1]), int(date[2]))

    difference_in_years = relativedelta(now, date).years

    if difference_in_years >= 18:
        return True

    return False


def main():
    u = get_usuarios()
    return [u[i] for i in u if is_adult(u[i]["data_nascimento"])]


print("Usuários maiores de idade:")
for usuario in main():
    print("{} ({})".format(usuario["nome"], usuario["data_nascimento"]))
