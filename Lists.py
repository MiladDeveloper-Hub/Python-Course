# list in python

item1 = "python"
item2 = "go"
item3 = "kotlin"
item4 = "java"

myList = [item1, item2, item3, item4]

print(myList[2])
print(len(myList))

print(len(myList) -1)

isKotlinInList = "kotlin" in myList
print(isKotlinInList)

print("---------------")

myRange = range(30)
print(list(myRange))