# zip()

numbers0 = [1, 2, 3, 4, 5]
numbers1 = [6, 7, 8, 9, 10, 11]

result = zip(numbers0, numbers1)

# print(list(result))

myList = [(1, 2), (3, 4), (5, 6), (7, 8)]

# print(list(zip(*myList)))

students = ["Milad", "Mohammad", "Iman"]
midterm = [74, 89, 95]
final = [86, 94, 84]

finalGrades = {ob[0]: max(ob[1], ob[2]) for ob in zip(students, midterm, final)}

print(f"Maximum is : {finalGrades}")

average = zip(
    students,
    map(
        lambda pair: pair[0] + pair[1] / 2,
        zip(midterm, final)
    )
)

print(f"Average is : {dict(average)}")