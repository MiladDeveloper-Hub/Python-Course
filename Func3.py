# Parametrs in def

def sum(number):
    return number + 10


print(sum(5))

print("----------------")


def sum(firstNumber, secondNumber):
    return firstNumber + secondNumber


print(sum(5, 10))

print("----------------")


def showFullName(firstName, lastName):
    return firstName + " " + lastName


print(showFullName("Milad", "Golchinpour"))

print("----------------")

# example : sum_odd_numbers

myNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def sum_odd_numbers(numbers):
    total = 0
    for num in numbers:
        if num % 2 != 0:
            total += num
    return total


print(sum_odd_numbers(myNumbers))

print("----------------")


# example : check even number

def is_even_number(number):
    if number % 2 == 0:
        return True
    return False


print(is_even_number(5))
