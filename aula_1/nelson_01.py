from requests import get

url = 'https://httpbin.org/uuid'


def get_uuid():
    result = get(url)
    return result.json()['uuid']


def main():
    print('O UUID é: {0}'.format(get_uuid()))


main()