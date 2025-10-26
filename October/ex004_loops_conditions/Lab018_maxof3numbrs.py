num1 = int(input("please enter number1"))
num2 = int(input("please enter number2"))
num3 = int(input("please enter number3"))

if num1 > num2 and num1 > num3:
    print(num1, "is maximum")
elif num2 > num1 and num2 > num3:
    print(num2, "is maximum")
elif num3 > num1 and num3 > num2:
    print(num3, "is maximum")
