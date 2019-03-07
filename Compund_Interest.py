''' Program to find the Compound Interest compounded annually and the total amount when the
Principal, Rate of Interest and Time are entered by the user'''
p = int(input("principal\n"))
r = float(input("rate\n"))
n = int(input("periods\n"))

c = p*((1+r)**n -1)
#user can change formula for compound interest according to their need.
print("compound interest",c)
