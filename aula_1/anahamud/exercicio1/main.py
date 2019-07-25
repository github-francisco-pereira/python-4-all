# virtualenv venv
# source venv/bin/activate
# pip install requests
# python main.py
# pip freeze -l > requirements.txt
# deactivate

import requests

response = requests.get('https://httpbin.org/uuid')

print('Your uuid is {0}'.format(response.json()['uuid']))