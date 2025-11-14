

def power_of_numbers(number):
    if number >= 0:
      return number * number
    else :
        return "please enter a positive number"


powernumber = power_of_numbers(int(input("enter a positive number: ")))
print(powernumber)
