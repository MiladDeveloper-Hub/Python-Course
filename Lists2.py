# lists in python

myList = [1, 2, 3, 4, 5, 6]

print(myList[5])

print("---------")

myCars = ["bmw", "pride", "benz", "tasla", "pejo", 405]

for car in myCars:
    if type(car) == str :
        print(f"String Car Name is {car}")
    else:
        print(f"Int Car Name is {car}")
print("-------------")
index = 0
while index < len(myCars) :
    carss = myCars[index]
    if type(car) == str :
            print(f"String Car Name is {car}")
    else:
        print(f"Int Car Name is {car}")
    index += 1