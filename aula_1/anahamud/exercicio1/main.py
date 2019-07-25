# virtualenv venv
# source venv/bin/activate
# pip install requests
# python main.py
# pip freeze -l > requirements.txt
# deactivate

# virtualenv venv2
# source venv2/bin/activate
# pip install -r requirements.txt
# python main.py
# deactivate

import requests

response = requests.get('https://httpbin.org/uuid')

print('Your uuid is {0}'.format(response.json()['uuid']))