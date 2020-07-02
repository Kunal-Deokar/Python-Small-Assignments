#Program for finding maximum of three numbers
print("Find maximum of 3 numbers here")

num1=int(input("\nEnter the first number:"))
num2=int(input("\nEnter the second number:"))
num3=int(input("\nEnter the third number:"))

if(num1>=num2):
    if(num1>=num3):
        print("\n\tMaximum number is:",num1)
    else:
        print("\n\tMaximum number is:",num3)

elif(num2>=num3):
    print("\n\tMaximum number is:",num2)

else:
    print("\n\tMaximum number is:",num3)


