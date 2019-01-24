''' Program to find the area and circumference of a circle, when the radius is entered by the user.
However, the user can input radius in integer or float'''
radius = float(input("Radius\n"))
pi = 3.14
area = pi*(radius**2)
circm = 2*pi*radius 
print(area)
print(circm)
