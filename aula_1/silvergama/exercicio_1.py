from requests import get

response = get('https://httpbin.org/uuid')
responseJson = response.json()
uuid = responseJson.get('uuid')

print('uuid atual: %s' % (uuid))