'''Program to find the hypotenuse of a right angled triangle, when the base and height are entered
by the user.'''
base = int(input("Base\n"))
height = int(input("Height\n"))
hypo = ((base**2) + (height**2))**0.5
print("Hypotenuse = ",hypo)

