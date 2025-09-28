
def sum_of_three(num1=100,num2=200,num3=300):
    return num1+num2+num3

input1=int(input("Enter a number1: \n"))
input2=int(input("Enter a number2: \n"))
input3=int(input("Enter a number3: \n"))
total = sum_of_three(input1,input2,input3)
print(total)

total2=sum_of_three(input1,input2)
print(total2)