#Program to calculate average and grade for 3 subjects marks are given for a student.
print("Calculate average and grade for 3 subject\'s marks are given")
name=input("\n\nEnter student\'s name :")
sub1=int(input("\nEnter 1st subject\'s marks out of 100 :"))
sub2=int(input("\nEnter 2nd subject\'s marks out of 100 :"))
sub3=int(input("\nEnter 3rd subject\'s marks out of 100 :"))

avg=(sub1 + sub2 + sub3)/3
print("\n\nSee grade below--->")
if(avg>=90):
    print("\n\t"+name+" got \"O\" grade")
elif(avg>=60 and avg<90):
    print("\n\t"+name+" got \"A\" grade")
elif(avg>=40 and avg<60):
    print("\n\t"+name+" got \"B\" grade")
elif(avg<40):
    print("\n\t"+name+" got \"C\" grade")
