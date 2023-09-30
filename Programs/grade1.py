eng_marks = int(input("enter your english marks: "))
math_marks = int(input("enter your math marks: "))
if eng_marks >=80 and math_marks >= 80:
    print("Grade: A")
elif eng_marks >=80 or math_marks >= 80:
    print("Grade: B")
else:
    print("Grade: C")