from requests import get as get_exerc1

url = "https://httpbin.org/uuid"
chamada = get_exerc1(url).json()
print(chamada.get('uuid'))
