people = [
    {
        'name': 'Robson',
        'nickname': "Walter Withe", 
        'date_of_birth': '01/10/1976' # sim o meu videogame era o Atari (raiz/root) :)
    },
    {
        'name': 'Ana Mara',
        'nickname': "Marinha", 
        'date_of_birth': '04/11/1975'
    },
    {
        'name': 'Maria Helena',
        'nickname': "Heleninha", 
        'date_of_birth': '04/11/1950'
    },
    {
        'name': 'Aparecida',
        'nickname': "Cida", 
        'date_of_birth': '21/11/1960'
    },
    {
        'name': 'Cibele',
        'nickname': "Cibelona", 
        'date_of_birth': '03/10/1990'
    },
    {
        'name': 'Tatiane',
        'nickname': "Tati", 
        'date_of_birth': '04/08/1996'
    },
    {
        'name': 'Priscila',
        'nickname': "Pri", 
        'date_of_birth': '15/10/2000'
    },
    {
        'name': 'Antonio',
        'nickname': "Tonhao", 
        'date_of_birth': '12/08/1945'
    },
    {
        'name': 'Donizete',
        'nickname': "Zete", 
        'date_of_birth': '22/10/1940'
    },
    {
        'name': 'Thiago',
        'nickname': "Primo", 
        'date_of_birth': '22/03/1990'
    }
]

def get_nicknames(list):
    return [person['nickname'] for person in list]


print(get_nicknames(people))
  
