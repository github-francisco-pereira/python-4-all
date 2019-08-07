from sympy import isprime

def find_prime_number(list):
    i = 0
    while i <= len(list) and not isprime(list[i]):
        i = i + 1
    
    return list[i]


print(find_prime_number(range(10)))    

# Como nada se cria tudo se copia :)
# pip3 install sympy


