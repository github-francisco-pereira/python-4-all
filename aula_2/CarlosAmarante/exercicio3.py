list_users = [
    {
        'name': 'Carlos Amarante',
        'nickname': "Carlinhos",
        'date_of_birth': '15/12/1997'
    },
    {
        'name': 'João Nascimento',
        'nickname': "Joãozinho",
        'date_of_birth': '16/11/1996'
    },
    {
        'name': 'Ronaldo Gomes',
        'nickname': "Ronaldinho",
        'date_of_birth': '14/10/1995'
    },
    {
        'name': 'Maria Eduarda',
        'nickname': "Duda",
        'date_of_birth': '06/06/1990'
    },
    {
        'name': 'Sabrina Silva',
        'nickname': "Sasa",
        'date_of_birth': '04/05/1991'
    },
    {
        'name': 'Cristina Cruz',
        'nickname': "Cris",
        'date_of_birth': '22/05/1997'
    },
    {
        'name': 'Gustavo Borges',
        'nickname': "Gu",
        'date_of_birth': '11/04/1999'
    },
    {
        'name': 'Hamilton Bernades',
        'nickname': "Hamilton",
        'date_of_birth': '02/07/2000'
    },
    {
        'name': 'Fatima Ferreira',
        'nickname': "Fa",
        'date_of_birth': '01/03/1984'
    },
    {
        'name': 'Ricardo Bueno',
        'nickname': "Bueno",
        'date_of_birth': '15/12/1997'
    }
]


def get_nicknames(list_users):
    return [user['nickname'] for user in list_users]


print(get_nicknames(list_users))
