from requests import get

uuid = get('https://httpbin.org/uuid')
print(uuid.text[11:51])
