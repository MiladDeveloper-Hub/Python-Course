# Handle Error

# try:
#     print(myName)
# except:
#     print("an error found")

def get(dict, key):
    try:
        return dict[key]
    except:
        return "an error found : no key found"


person = {
    "name": "milad",
    "family": "golchinpour"
}

# print(get(person, "age"))
#
# while True:
#     print("Hello World !$!$!")
#     try:
#         num = int(input("Please enter a number to save in my computer : "))
#     except:
#         print("You not enter a number ! ")
#     else:
#         print(f"You enter {num}")
#         break
#     finally:
#         print("This is a input")


def divide(first, second):
    try:
        return first / second
    except ZeroDivisionError as error:
        print(error)
        return "Please don't enter zero division !!!"
    except TypeError as error:
        print(error)
        return "You not enter first and second number !!!"


print(divide(1, 0))
