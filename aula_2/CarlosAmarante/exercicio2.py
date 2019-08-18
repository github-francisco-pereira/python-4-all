def is_prime(current_number):
    if current_number == 1:
        return False
    elif current_number == 2:
        return True
    else:
        for ranged_number in range(2, current_number):
            return current_number % ranged_number != 0


LIST_NUMBER = list(range(1, 11))
get_out = False
count = 0
while count < LIST_NUMBER[-1] and get_out is not True:
    if is_prime(LIST_NUMBER[count]):
        print(LIST_NUMBER[count])
        get_out = True
    count += 1
