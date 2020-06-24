def power(number, power=2):
    return number ** power


print(power(2, 3))  # 2 * 2 * 2 = 8
print(power(3))  # 3 * 2 = 9


print("------------------")


def showFullName(first, last):
    return f"{first} {last}"


print(showFullName(last="Golchinpour", first="Milad"))
