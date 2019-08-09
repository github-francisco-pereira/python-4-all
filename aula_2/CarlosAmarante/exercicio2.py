def is_prime(current_number):
    if current_number <= 1:
        return False
    else:
        auxiliar_number = current_number - 1
        i = 2
        while (1 < i and i <= auxiliar_number):
            if current_number % i == 0:
                return False
            i += 1
        print(current_number)
        return True


x = list(range(1, 11))
get_out = False
count = 0
while count < x[-1] and get_out is not True:
    is_prime(x[count])
    count += 1
