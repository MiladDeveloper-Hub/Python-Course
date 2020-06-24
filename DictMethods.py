me = {
    "name": "milad",
    "family": "golchinpour",
    "age": 14,
    "email": "miladgolchinpour85@gmail.com"
}

print(me)

print("-------------")

# .clear()
# me.clear()
print(me)

print("-------------")

# .copy()
copyMe = me.copy()
print(copyMe)

print("-------------")

# for generated default values
# .fromkeys()
newUser = {"name": "unknown", "family": "unknown"}
newUser_2 = dict.fromkeys(["name", "family"], "unknown")
print(newUser_2)

# .get()
isExistPhone = me.get("phone")
print(isExistPhone is None)
