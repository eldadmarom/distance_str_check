def distance(num1, num2, num3):
    num1 = int(num1)
    num2 = int(num2)
    num3 = int(num3)
    con1 = abs(num1 - num2) == 1 and abs(num1 - num3) >= 2 and abs(num2 - num3) >= 2
    con2 = abs(num1 - num3) == 1 and abs(num1 - num2) >= 2 and abs(num2 - num3) >= 2
    if con1 or con2:
        print("True")
    else:
        print("False")
    return 

num1 = abs(int(input("Enter the first number: ")))
num2 = abs(int(input("enter the second number: ")))
num3 = abs(int(input("enter the third number: ")))

distance(num1, num2, num3)
