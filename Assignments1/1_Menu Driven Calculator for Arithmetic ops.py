#Menu Driven Calculator for Arithmetic operations
print("Arithmetic Calculator")
num1=int(input("\nEnter the first number:"))
num2=int(input("\nEnter the second number:"))
         
ch=input("\nEnter S for Menu:")
if(ch=="s" or ch=="S"):
    print("\t1.Add\n\t2.Subtract\n\t3.Multiply\n\t4.Division")
    choice=int(input("\nEnter your Choice:"))
    if(choice==1):
        print("\n\tSum = ",num1+num2)
    elif(choice==2):
        print("\n\tSubtraction = ",num1-num2)
    elif(choice==3):
        print("\n\tMultiplication = ",num1*num2)
    elif(choice==4):
        print("\n\tDivision = ",num1/num2)
    else:
        print("\n\tBad input")
    
         
        
    
            
