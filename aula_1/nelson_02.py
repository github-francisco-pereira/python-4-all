def divisor(valor):
    if valor % 3 == 0 and valor % 5 == 0:
        return 'fizzbuzz'
    if valor % 3 == 0:
        return 'fizz'
    if valor % 5 == 0:
        return 'buzz'  


print(divisor(3))
print(divisor(5))
print(divisor(15))
