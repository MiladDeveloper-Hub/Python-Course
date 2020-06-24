# tuple

myNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

tupleNumbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, (3, 4, 8))

print(3 in tupleNumbers)

print("--------------")

newTuple = tuple([1, 2, 3, 4, 5])

locations = {
    (35.45, 45.62): "Mountain View",
    (63.96, 56.79): "New York"
}

print(locations[35.45, 45.62])

print("--------------")

# for
for num in tupleNumbers:
    print(num)

print("--------------")

# .count()
print(tupleNumbers.count(3))

print("--------------")

# .index()
print(tupleNumbers.index(3))

print("--------------")

# 2 index
print(tupleNumbers[9][1])

print("--------------")

# slicing
print(tupleNumbers[2:5])
