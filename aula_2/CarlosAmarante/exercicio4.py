from datetime import datetime, date


def is_greater_than_18(birthday):
    current_time = datetime.now()
    age = current_time.year - birthday.year - (
        (current_time.month, current_time.day) < (birthday.month, birthday.day)
        )
    return age >= 18


list_users = []
for i in range(1000):
    list_users.append({
        'name': 'Name' + str(i),
        'nickname': 'nickname_' + str(i),
        'birthday':  date(datetime.now().year - i, 5, 9)
    })

adults = [user['name'] for user in list_users if is_greater_than_18(
    user['birthday'])]
print(adults)
