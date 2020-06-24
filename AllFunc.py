# all() in python

numberList = [2, 4, 6, 8, 10, 12, 14, 16, 18]
trueNumbers = [1, 2, 3, 4, 5, 6, 7]
falseNumbers = [0, 1, 2, 3, 4, 5, 6]

check0 = all(trueNumbers)
check1 = all(falseNumbers)

print(f"[1, 2, 3, 4, 5, 6, 7] True sines is : {check0}\n[0, 1, 2, 3, 4, 5, 6] False sines is : {check1}")

even = all(num for num in numberList if num % 2 == 0)

print(f"Even ?? : {even}")
