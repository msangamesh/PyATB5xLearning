 # function types
 # no argument function
 # argument function
 # default value function
 # return value function

# no argument function

def greet_to_all():
    print("Hello, Welcome to Python!")

# argument function

def greet_by_name(name):
    print("Hello, "+ name + "!")
# greet_by_name("Sangareddy")

 # default value function

def mul_greet_by_name(name1="Sangareddy", name2="Munge"):
    print("Hello, "+ name1 ,name2)
    print(name2.upper())
# mul_greet_by_name("Munge","reddy")
# mul_greet_by_name("Sangareddy")
# mul_greet_by_name(name2="reddy")

# return value function

def sum_oftwo(num1, num2):
    return num1 + num2

num1input = int(input("Enter a number1: \n"))
num2input = int(input("Enter a number2: \n"))
total = sum_oftwo(num1input,num2input)
print(total)








