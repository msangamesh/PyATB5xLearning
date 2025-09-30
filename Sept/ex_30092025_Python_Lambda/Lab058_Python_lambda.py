

# def find_even_odd(num):
#     if num % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")


input_num = int(input("Enter a number:\n "))
# find_even_odd(input_num)

oddeven = lambda num: "Even" if num % 2 == 0  else "Odd"
print(oddeven(input_num))