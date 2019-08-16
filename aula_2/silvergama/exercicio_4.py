# Exercício 4
# Crie um arquivo .py que tenha um dicionario com 100 usuários.
# O dicionário deve conter as chaves: `nome`, `apelido` e `data_nascimento`.
# Crie uma função que retorne somente usuários maiores de idade.

from datetime import datetime, date
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta
from random import randint


def create_persons():
    persons = []
    for i in range(1, 101):
        person = {
            "name": "Name_{}".format(i),
            "nickname": "Nickname_{}".format(i),
            "date_of_birth": random_date()
        }
        persons.append(person)
    return persons


def random_date():
    day_of_the_year = randint(1, 366)
    year = randint(1980, 2018)
    date_str = '{} {}'.format(day_of_the_year, year)
    return datetime.strptime(date_str, '%j %Y').strftime('%Y-%m-%d')


def get_legal_age_persons(persons):
    legal_age_persons = []
    for person in persons:
        if is_legal_age(person['date_of_birth']):
            legal_age_persons.append(person)
    return legal_age_persons


def is_legal_age(date_of_birth):
    age = relativedelta(
        date.today(), parse(date_of_birth)
    ).years
    return age >= 18


persons = create_persons()
print(get_legal_age_persons(persons))
