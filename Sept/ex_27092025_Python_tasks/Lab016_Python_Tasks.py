num1 = int(input("Enter a number 1: "))
num2 = int(input("Enter a number 2: "))

mod = divmod(num1, num2)
print("The Quotient is:", mod[0])
print("The Remainder is:",mod[1])