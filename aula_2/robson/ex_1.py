odd_numbers = [ number for number in range(0, 1000) if not number % 2 == 0]

result = sum(odd_numbers)

print(result)