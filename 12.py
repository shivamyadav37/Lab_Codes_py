''' Program to find the Simple Interest and the total amount when the Principal, Rate of Interest
and Time are entered by the user.'''
p = int(input("principaal\n"))
r = float(input("rate\n"))
t = int(input("time\n"))

si = (p*r*t)/100
print("simple interest",si)
