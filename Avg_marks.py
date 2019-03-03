# Take in the marks of 5 subjects and display the grade.
sub1=int(input("Enter the marks in First subject\n"))
sub2=int(input("Enter the marks in Second subject\n"))
sub3=int(input("Enter the marks in Third subject\n"))
sub4=int(input("Enter the marks in Fourth subject\n"))
sub5=int(input("Enter the marks in Fifth subject\n"))

avg= (sub1+sub2+sub3+sub4+sub5)/5
if(avg>90):
    print("Grade: A")
elif(avg>=80):
    print("Grade: B")
elif(avg>=70):
    print("Grade: C")
elif(avg>=60):
    print("Grade: D")
elif(avg>=50):
    print("Grade: E")
else:
    print("Grade: F")
