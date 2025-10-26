#Given a number you need to calculate the factorial of number

num = int(input("Enter a number: "))

i = num
while i > 0:

    i = i - 1
    fact_res = num * i
    num = fact_res

    if i == 1:
        print("The factorial of number is", fact_res)


