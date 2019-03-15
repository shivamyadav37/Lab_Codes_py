''' Program to find whether a triangle is scalene, isosceles, right angled or invalid when the sides of the triangle are entered by the user.'''
a = int(input("1st side\n"))
b = int(input("2nd side\n"))
c = int(input("3rd side\n"))
if (a**2) == ((b**2 + c**2)):
	print("right angled")

elif a==b or a==c or b==c:
	print("isosceles")
else:
#elif a!=b!=c:
	print("scalene")
