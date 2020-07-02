#Program to find the root of the quadratic equation
print("Find the root of the Quadratic equation here")
a=int(input("\nEnter the co-efficient of the square term:"))
b=int(input("\nEnter the co-efficient of the variable term:"))
c=int(input("\nEnter the constant term:"))
discriminant=((b**2)-(4*a*c))
if(discriminant<0):
    print("\n\tNo real roots")
elif(discriminant==0):
    print("\n\tEquation has only one root\n\tRoot = ",(-b)/(2*a))
elif(discriminant>0):
    print("\n\tEquation has two real roots\n\tRoot1 = ",((-b)+((b**2)-(4*a*c))**(1/2))/(2*a))
    print("\n\tRoot2 = ",((-b)-((b**2)-(4*a*c))**(1/2))/(2*a))
      
