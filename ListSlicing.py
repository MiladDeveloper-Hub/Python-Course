# list slicing in python => to make a copy from a list :)

myList = [1, 2, 3, 4, 5, 6, 7, 8, 9]

selctedNumber = myList[1]

print(selctedNumber)

# Some_List @@@@ **** $$$$ #### ======>>>> [start:stop:step] @@@ ###

selctedNumbersFromList = myList[1:7:1]

print(selctedNumbersFromList)

# make a copy from a list

CopyList = myList[:]

print(CopyList)

print(myList == CopyList)
print(myList is CopyList)

# reverse with slicing
copyWithSc = myList[::-1]
print(copyWithSc)

