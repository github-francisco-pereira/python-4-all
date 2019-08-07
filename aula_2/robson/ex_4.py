from datetime import date

people = []

for i in range(100):
    people.append(
        {
            'name': f'name_{i}',
            'nickname': f'nickname_{i}',
            'date_of_birth': date(2019 - i, 8, 8)
        }
    )


def get_adults(list):
    return [person for person in list if get_age(person['date_of_birth']) >= 18] 

# Ok ! peguei no google essa func :)
def get_age(date_of_birth):
    today = date.today()
    age = today.year - date_of_birth.year - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))

    return age
 
  
for person in get_adults(people):
    print(person['date_of_birth'])
