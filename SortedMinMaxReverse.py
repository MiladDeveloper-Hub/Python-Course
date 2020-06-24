# sorted()

numbers = [1, 3, 2, 6, 5, 4]

print(sorted(numbers))

users = [
    {"name": "ali", "family": "moradi", "age": 23},
    {"name": "milad", "family": "moradi", "age": 62},
    {"name": "taha", "family": "moradi", "age": 21}
]

print(sorted(users, key=lambda user: user["age"]))

print("---------------")

# max()

myNumbers = [-2414121, 3, 2, 6, 5, 4, 2423, 2423.001, 45]

chars = ["t", "a", "x"]

Name = "milad"

print(max(Name))

names = ["milad", "mohammad", "iman", "zahra"]

print(max(names, key=lambda name: len(name)))

print("---------------")

# min()

print(min(myNumbers))

names = ["milad", "mohammad", "iman", "zahra"]

print(min(names, key=lambda name: len(name)))

print("---------------")

# reversed()

numS = [1, 2, 3, 4, 5, 6]

print(list(reversed(numS)))

nameRes = ""

print(nameRes.join(reversed("milad")))

for num in reversed(range(0, 11)):
    print(num)
