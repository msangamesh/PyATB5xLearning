 # find the type of triangle

side1 = int(input("Enter the side length of side1: "))
side2 = int(input("Enter the side length of side2: "))
side3 = int(input("Enter the side length of side3: "))

if (side1 == side2) and (side1 == side3) and (side2 == side3):
 print("Triangle type is:", "Equilateral")
elif (side1 == side2) or (side1 == side3) or  (side2 == side3):
 print("Triangle type is:", "Isosceles")
else:
 print("Triangle type is:", "scalene")

