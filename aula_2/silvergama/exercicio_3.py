# Exercício 3
# Crie um arquivo .py que tenha um dicionario com 10 usuários.
# O dicionário deve conter as chaves: `nome`, `apelido` e `data_nascimento`.
# Crie uma função que retorne somente uma lista com os apelidos.

persons = [
    {
        "name": "Lorenzo",
        "nickname": "Lo",
        "date_of_birth": "22-01-2014"
    },
    {
        "name": "Silver",
        "nickname": "Prata",
        "date_of_birth": "14-04-1988"
    },
    {
        "name": "Ariane",
        "nickname": "Nani",
        "date_of_birth": "21-06-1982"
    },
    {
        "name": "Marcio",
        "nickname": "Ma",
        "date_of_birth": "01-01-1990"
    },
    {
        "name": "Rodolfo",
        "nickname": "Ro",
        "date_of_birth": "01-02-1989"
    },
    {
        "name": "Gisele",
        "nickname": "gi",
        "date_of_birth": "06-03-1983"
    },
    {
        "name": "Fernanda",
        "nickname": "Fe",
        "date_of_birth": "03-05-1984"
    },
    {
        "name": "Fernando",
        "nickname": "Nando",
        "date_of_birth": "04-06-1994"
    },
    {
        "name": "Vitor",
        "nickname": "Vitão",
        "date_of_birth": "30-03-1970"
    },
    {
        "name": "Victoria",
        "nickname": "Vic",
        "date_of_birth": "20-04-1980"
    }
]


def get_nickname(person):
    return person['nickname']

nicknames = [get_nickname(person) for person in persons]
print(nicknames)
