def check_fizzbuzz(number):
    result = ''
    
    if number % 3 == 0:
        result += 'fizz'
    
    if number % 5 == 0:
        result += 'buzz'
    
    if result == '':
        result += 'The number cannot be divided by 3 or 5 = ['
    
    return result

fizzbuzz = check_fizzbuzz(15)
print(fizzbuzz)