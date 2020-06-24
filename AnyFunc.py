# any() in python

numbers = [2, 4, 6, 3]

result = [False, False, False, False]

check = any([num % 2 != 0 for num in numbers])

print(check)
