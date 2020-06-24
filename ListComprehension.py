myNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

doubleNumbers = [num * 2 for num in myNumbers]
print(doubleNumbers)

print("---------------------")

myName = "milad"
myNameChar = [char.upper() for char in myName]
print(myNameChar)

print("---------------------")

even = [num for num in myNumbers if num % 2 == 0]
odd = [num for num in myNumbers if num % 2 != 0]

print(f"Even Numbers are : {even}\nOdd Numbers are : {odd}")

newList = [num * 2 if num % 2 == 0 else num * 3 for num in myNumbers]
print(newList)