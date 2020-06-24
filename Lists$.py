# lists in the python

# index()
myCourses = ["Python", "Java", "Go", "Python", "Kotlin", "JavaScript", "VueJs"]
myNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
unSort_numbers = [5, 7, 1, 9, 3, 4, 2, 8, 6]

indexKotlin = myCourses.index("Kotlin")
indexGo = myCourses.index("Go")
indexPython = myCourses.index("Python", 1, 5)

print(f"Index Of Kotlin is : {indexKotlin}")
print(f"Index Of Go is {indexGo}")
print(f"Index Of Python is : {indexPython}")

print("-------------------")

# count()
numberOfPython = myCourses.count("Python")
print(numberOfPython)

print("-------------------")

# reverse()
myNumbers.reverse()
print(myNumbers)

print("-------------------")

# sort()
unSort_numbers.sort()
print(unSort_numbers)

print("-------------------")

# join()
myJoin = " | " .join(myCourses)
print(myJoin)