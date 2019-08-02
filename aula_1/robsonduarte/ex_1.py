import requests

def get():
   response = requests.get('https://httpbin.org/uuid')
   print(response.text)


get()   