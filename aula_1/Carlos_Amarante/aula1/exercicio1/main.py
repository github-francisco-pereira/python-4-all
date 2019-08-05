from requests import get


response = get('https://httpbin.org/uuid')
print('uuid field is {0}'.format(response.json()['uuid']))
