# dict {
#   key: value
#   ....
# }

myDict = {
    "name": "python",
    "isRecord": True,
    "price": 120
}

myDict_2 = dict(name="milad", age="14")

print(myDict)

print("---------------")

me = {
    "name": "Milad",
    "family": "Golchinpour",
    "age": 14
}

print("------------")

# .values()
for value in me.values():
    print(value)

print("------------")

print(me.values())


print("------------")


# .keys()
for key in me.keys():
    print(key)

print("------------")

print(me.keys())


print("------------")


# .items()
for key, value in me.items():
    print(key, value)

print("------------")

print(me.items())
