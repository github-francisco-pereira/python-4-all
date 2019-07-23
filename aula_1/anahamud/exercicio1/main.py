import requests

response = requests.get('https://httpbin.org/uuid')

print('Your uuid is {0}'.format(response.json()['uuid']))