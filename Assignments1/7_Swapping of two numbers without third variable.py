#Program to Swap two numbers without third variable
print("Swapping of two numbers without use of third variable")
n1=int(input("\nEnter the Number1 :"))
n2=int(input("\nEnter the Number2 :"))
print("\n\tValues before swapping-->\n\t\tNumber1 = ",n1,"\n\t\tNumber2 = ",n2)

m=int(input("\nSelect the method:\n\t1.Built-in\n\t2.Bitwise XOR\n\t3.Additon & Subtraction\n\t4.Multiplication & Division\n\t:"))
if(m==1):
    #Built-in method
    n1,n2=n2,n1
    print("\n\tValues after swapping using \"BUILT-IN METHOD\"-->\n\t\tNumber1 = ",n1,"\n\t\tNumber2 = ",n2)
elif(m==2):
    #Biwise XOR method
    n1^=n2
    n2^=n1
    n1^=n2
    print("\n\tValues after swapping using \"BITWISE XOR METHOD\"-->\n\t\tNumber1 = ",n1,"\n\t\tNumber2 = ",n2)
elif(m==3):
    #Additon & Subtraction method
    n1=n1+n2
    n2=n1-n2
    n1=n1-n2
    print("\n\tValues after swapping using \"ADDITION & SUBTRACTION METHOD\"-->\n\t\tNumber1 = ",n1,"\n\t\tNumber2 = ",n2)
elif(m==4):
    #Multiplication & Division Method
    n1=n1*n2
    n2=n1/n2
    n1=n1/n2
    print("\n\tValues after swapping using \"MULTIPLICATION & DIVISION METHOD\"-->\n\t\tNumber1 = ",n1,"\n\t\tNumber2 = ",n2)
else:
    print("\n\tInvalid Choice!!!")

