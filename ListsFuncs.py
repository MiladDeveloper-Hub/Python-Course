# functions of list in python

myCourses = ["Python", "Kotlin", "Java", "JavaScript"]
myCourses2 = ["VueJs", "JQuary"]

print(myCourses)

print("----------------------")

myCourses.append("Blander")

print(myCourses)
print(len(myCourses))

myCourses.append(myCourses2)

print(myCourses)
print(len(myCourses))

myCourses.extend(["Asp.net", "C#"])

print(myCourses)
print(len(myCourses))

myCourses.insert(1, "C++")

print(myCourses)
print(len(myCourses))

myCourses.insert(-1, "C")

print(myCourses)
print(len(myCourses))