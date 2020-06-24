# map() in python

numbers = [1, 2, 3, 4, 5]

# Convert to doubles

print("------------------")

# Way 1
doubles1 = [2, 4, 6, 8, 10]

print("------------------")

# Way 2
for num in numbers:
    doubles1.append(num * 2)
print(doubles1)

print("------------------")

# Way 3
doubles3 = map(lambda x: x * 2, numbers)
print(list(doubles3))
print(list(doubles3))
# map => only once control items

print("------------------")

names = ["milad", "mohammad", "amin", "sars"]

upperNames = map(lambda name: name.upper(), names)

print(list(upperNames))

# a best example

people = [
    {"name": "Milad", "family": "Golchinpour", "age": 14},
    {"name": "Amin", "family": "Kokabi", "age": 14},
    {"name": "Ali", "family": "Moradi", "age": 14}
]

familyList = map(lambda person: person["family"], people)

print(list(familyList))
