me = {
    "name": "milad",
    "family": "golchinpour",
    "age": 14,
    "email": "miladgolchinpour85@gmail.com"
}

isExistEmail = "email" in me

print(f"Email : {isExistEmail}")

isExistAddress = "addres" in me

print(f"Address : {isExistAddress}")

if "email" in me:
    print("True")
else:
    print("False")

print("----------------")

isExistMilad = "milad" in me.values()

print(isExistMilad)

