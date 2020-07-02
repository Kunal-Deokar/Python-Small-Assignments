"""To calcualte electricty bill, read unit from user and do calculation
   unit <=100  calcualte bill @3rs perunit
   unit>100 and unit <= 500  calcualte bill @ 5rs perunit
   unit>500 and unit <=1000  calcualte bill @ 9rs perunit
   unit >1000  calcualte bill @11rs perunit"""
print("Program to calculate Electricity Bill")

units=int(input("\nEnter the units consumed :"))

if(units<=100):
    print("\n\tYour Electricity Bill is ",units*3," Rs")
elif(units>100 and units<=500):
    print("\n\tYour Electricity Bill is ",units*5," Rs")
elif(units>500 and units<=1000):
    print("\n\tYour Electricity Bill is ",units*9," Rs")
elif(units>1000):
    print("\n\tYour Electricity Bill is ",units*11," Rs")
