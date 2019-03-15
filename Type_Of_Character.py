#Author--> Shivam Yadav
#Problem--> Program to determine the character entered by user. 

#Program-->

n=input("Press any Key\n")
if(n.isalpha()):
    print("The user has entered a character")
if(n.isdigit()):
    print("The user has entered a Digit")
if(n.isspace()):
    print("The user has entered a White space Character")
