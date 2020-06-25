# claculator project

print("Hello User, Welcome To My Calculator :)...")
number = int(input("Please enter first number : "))
number1 = int(input("Please enter second number : "))
oper = input("Please enter operator ( +  -  *  / ) : ")

if oper == "+":
    print(f"Sum numbers is : {number + number1}")
elif oper == "-":
    print(f"Subtraction numbers is : {number - number1}")
elif oper == "*":
    print(f"Multiply numbers is : {number * number1}")
elif oper == "/":
    print(f"Divide numbers is : {number / number1}")
else:
    print("Somethings Went Wrong ! :( ")