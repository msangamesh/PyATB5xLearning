# grade calculate

score = float(input("Enter your score: ").strip())

if score <= 0 and score > 100:
    print("please enter valid score")
else:
    if score >= 90 and score <= 100:
        print("your grade is A")
    else:
        if score >= 80 and score < 90:
            print("your grade is B")
        else:
            if score >= 70 and score < 80:
                print("your grade is C")

