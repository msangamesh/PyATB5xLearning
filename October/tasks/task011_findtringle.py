
side1 =int(input("enter a side 1: "))
side2 =int(input("enter a side 2: "))
side3 =int(input("enter a side 3: "))

def find_triangle(side1,side2,side3):
    if (side1 == side2 and side1 == side3 and side2 == side3 ):
        print("the tringle is isosceles")
    else:
        if (side1 == side2 or side2 == side3  or side3 == side1 ):
            print("the tringle is equilateral")
        else :
              print("the tringle is scalene")


tringletype = find_triangle(side1,side2,side3)
print(tringletype)





