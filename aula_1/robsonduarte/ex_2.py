def fizz_buzz(num):
    result = ''
    if num % 3 == 0:
        result = 'fizz'
    if num % 5 == 0:
        result = 'buzz'
    if num % 3 == 0 and num % 5 == 0:
        result = 'fizzbuzz'
    print(result)


fizz_buzz(9)
fizz_buzz(10)
fizz_buzz(15)