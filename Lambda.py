# a other way to create a function

# way 1
def squre(num): return num * num


print(squre(5))

# way 2
squre2 = lambda num: num * num

print(squre2(5))

print("--------------")

# example way 2
sumNumbers = lambda first, second: first + second

print(sumNumbers(5, 10))

print("---------------")

# lambda not has __name__

print(squre.__name__)
print(squre2.__name__)
