# *args

def sumAllNumbers(*args):
    print(args)
    total = 0
    for num in args:
        total += num
    return total


numbers = [1, 2, 3, 4, 5, 6]

print(sumAllNumbers(*numbers))
# print(sumAllNumbers("first : ", 1, 1, 1))
# print(sumAllNumbers("second : ", 2, 2, 2))
# print(sumAllNumbers("third : ", 3, 3, 3))

print("---------------")


# **Kwargs


def user_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")


user_info(name="Milad", family="Golchinpour", age="14", email="miladgolchinpour85@gmail.com")

print("---------------")


def name_family(name, family):
    print(f"name is {name} and family is {family}")


person = {
    "name": "Milad",
    "family": "Golchinpour"
}

print(name_family(**person))

print("---------------")


# all in one

# to all in one :
# 1 - parameters
# 2 - *args
# 3 - default parameter
# 4 - **kwargs

# example :
def info(firstNumber, secondNumber, *args, defPar="A Default Parameter", **kwargs):
    return [firstNumber, secondNumber, args, defPar, kwargs]


print(info(1, 2, "Hi", name="Milad", family="Golchinpour"))
