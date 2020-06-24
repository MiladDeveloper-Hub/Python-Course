me = {
    "name": "milad",
    "family": "golchinpour",
    "age": 14,
    "email": "miladgolchinpour85@gmail.com"
}

print(me)

print("------------")

# .pop()
# me.pop("name")
# print(me)

print("------------")

# .popitem()
# me.popitem()
# print(me)

print("------------")

# .update()

secondDict = {
    "name": "milad"
}

secondDict.update(me)

print(secondDict)

print("--------------------")

secondDict["name"] = "sara"

print(secondDict)
