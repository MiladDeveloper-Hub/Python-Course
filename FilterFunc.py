# filter()

numbers = [1, 2, 3, 4, 5, 6]

evens = filter(lambda num: num % 2 == 0, numbers)
odds = filter(lambda num: num % 2 != 0, numbers)

print(f"Even numbers are : {list(evens)}\nOdd numbers are : {list(odds)}")

# other example

users = [
    {
        "name": "milad",
        "shopCart": ["python", "go"]
    },
    {
        "name": "amin",
        "shopCart": []
    },
    {
        "name": "ali",
        "shopCart": []
    }
]

# print(len(users))
#
# result = filter(lambda user: not user["shopCart"], users)
#
# print(list(result))

# result = map(lambda user: user["name"],
#              filter(lambda user: not user["shopCart"], users)
#              )
#
# print(list(result))

result = [user["name"] for user in users if not user["shopCart"]]

print(result)

