
import requests
from operator import itemgetter

url = 'https://httpbin.org/uuid'

site = requests.get(url)
dados = site.json()

for key, value in dados.items():
    print (key)

#print (list(map(itemgetter(0), dados.items())))

