#Author--> Shivam Yadav
#Problem-->
# Write a program to calculate area of a triangle using Heron's Formula

#Program-->
a=float(input("Enter the first side of triangle\n"))
b=float(input("Enter the second side of triangle\n"))
c=float(input("Enter the third side of triangle\n"))

#print(a,b,c)
s=(a+b+c)/2

area=(s*(s-a)*(s-b)*(s-c))**0.5

print("Area =",area)
