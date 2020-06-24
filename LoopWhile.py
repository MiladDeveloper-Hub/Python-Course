# While

passwd = input("Please enter a password : ")

print("Ok, Password Seved")

password = input("Please enter your password : ")

while password != passwd:
    print("Wrong Password ! :( ")
    password = input("Please re enter your password : ")
    if password == passwd:
        print("\nLogin Succesfull :) ")


num = 1
while num <= 10:
    print("*" * num)
    num += 1
    if num == 5:
        break
print("This is over")