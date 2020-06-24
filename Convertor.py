# a km to mile convertor

def hello():
    print("\nHello User :)\n\nThis App Convert Km To Mile\n")

hello()

kmInput = float(input("Please enter mile to covert to km : "))

covertedNumber = float(kmInput) / 1.60934

mile = round(covertedNumber, 3)

print(f"\nOk, Converted : {kmInput} Km is {mile} Mile !")