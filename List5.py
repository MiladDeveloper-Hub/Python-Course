# nested lists

myNumbers = [[1, 2, 3], [4, 5, 6]]

# way 1
index_1 = myNumbers[1]
index_1_ofMyNumbers = index_1[1]

# way 2
number = myNumbers[1][1]

print(number)

print("----------------------")

for lis in myNumbers:
    for num in lis:
        print(num)

print("----------------------")

copyList = [[print(l) for l in li] for li in myNumbers]

# print(copyList)

print("----------------------")

# Nested List in for

generatedList = [num for num in range(1, 6)]
generatedNestedList = [[newNum for newNum in range(1, 6)] for num in range(1, 6)]

print(generatedNestedList)

print("----------------------")

generatedNestedList = [['Even' if newNum % 2 == 0 else 'Odd' for newNum in range(1, 6)] for num in range(1, 6)]

print(generatedNestedList)