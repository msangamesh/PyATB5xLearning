score  = int(input ('Enter a score: \n'))

if score >= 90 :
    print ("Your grade is:", "A")
elif score >= 80 and score < 90:
    print ("Your grade is:", "B")
elif score >= 70 and score <= 79:
    print ("Your grade is:", "C")
elif score >= 60 and score < 70:
    print ("Your grade is:", "D")
else :
    print ("Your grade is:", "F")

