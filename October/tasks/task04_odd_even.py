# find the even odd number
# strip removes the extra spaces in input
num = int(input("enter the number").strip())

if num >= 0:
    if num % 2 == 0:

        print(num, "is even")
    else:
        print(num, "is odd")
else :
    print(num, "is negative")