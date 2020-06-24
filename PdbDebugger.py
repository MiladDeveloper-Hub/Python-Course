# import pdb
#
# pdb.set_trace()
#
# print("Hello user, this is a summer")
# number1 = int(input("Please enter first number"))
# number2 = int(input("Please enter second number"))
# res = number1 + number2
# print(f"Result is {res}")

# pdb commands
# l => show list of your commands
# n => new line
# c => continue => finished the python debugger
# p =>

def add_numbers(a, b, c, d):
    import pdb
    pdb.set_trace()
    return a + b + c + d

print(add_numbers(1,2,3,4))
