# set in python

myNumbers = {1, 2, 3, 4, 5, 6, 6, 5, 2, 3}

# numbers_2 = {3, 4, 5, 'g', 'z'}
#
# print(myNumbers)
#
# print("------------")
#
# print(4 in myNumbers)
#
# print("------------")
#
# print(numbers_2)
#
# print("------------")
#
# # for
# for item in numbers_2:
#     print(item)
#
# print("------------")
#
# # set class
# # convert list to set
# courses = ['Kotlin', 'Python', 'Dart','Flutter', 'Go', 'Java']
# myCourses = set(courses)
# print(myCourses)
#
# print("------------")
#
# # convert set to list
# print(list(numbers_2))

# .add()
# myNumbers.add(5)
# print(myNumbers)

# .remove()
# myNumbers.remove(2)
# print(myNumbers)

# .discard()
# myNumbers.discard(4)
# print(myNumbers)

# .copy()
# copyNumbers = myNumbers.copy()
# print(myNumbers == copyNumbers)
# print(myNumbers is copyNumbers)
# print(copyNumbers)

# .clear()
# myNumbers.clear()
# print(myNumbers)

# VEEEEEEEEEEEEEERYYYYYYYYY ITERSPECT

# " | " and " & " is set
# python = {"ali","milad","mohammad","sara", "reza"}
# dart = {"reza","mina","alireza","mehdi","ali"}

# " | "
# print(python | dart)

# " & "
# print(python & dart)

# set compare

# example 1
newNum = {x ** 2 for x in range(10)}
print(newNum)

print("--------------------------")

# example 2
myName = {char for char in "Hello World"}
print(myName)