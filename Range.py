# range => create a list of numbers
# 1, 2, 3, 4, 5, ..., 10

print(list(range(1, 10))) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(10))) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(1, 10, 2))) # [1, 3, 5, 7, 9]
print(list(range(10, 0, -1))) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

print("------------------------------------")

for number in range(1,10):
    print("*" * number)

# Example :

for num in range(1,10):
    if num % 2 != 0:
        for star in range(1,5):
            print("*" * star)
    else:
        for star in range(5,0,-1):
            print("*" * star)
