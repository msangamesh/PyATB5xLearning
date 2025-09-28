

side1 = int(input("Enter the side length of side1: "))
side2 = int(input("Enter the side length of side2: "))
side3 = int(input("Enter the side length of side3: "))

def type_triangle(s1, s2, s3):

 if s1 > 0 and s2 >0 and s3>0:
    if s1+s2 >s3 and s1+s3 >s2 and s2+s3 >s1:

      if (s1 == s2) and (s1 == s3) and (s2 == s3):
        return "Equilateral"
      elif (s1 == s2) or (s1 == s3) or (s2 == s3) :
        return "Isosceles"
      else :
            return "Scalene"

    else :
     return "Not a triangle"
 else :
        return "Not a valid length"



result = type_triangle(side1, side2, side3)
print (f"Triangle type is: {result}")

