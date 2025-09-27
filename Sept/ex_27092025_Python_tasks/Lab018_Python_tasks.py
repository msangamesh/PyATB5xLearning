import math  # program to calculate area of the circle if radius is given

radius = float(input("enter radius:\n"))

# area = 3.14 *( radius ** 2)
#
# # print("Area of the circle is:",area)
#
# print(f"Area of the circle is: {area:.4f}")

import math

area = math.pi * math.pow(radius, 2)
print(f"Area of the circle is: {area:.4f}")

