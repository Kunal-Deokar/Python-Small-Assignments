"""Program to find where enter character is upper case, lower case, digit, 
space , tab, single quot, double quot or special character"""
print("Finding the character type entered by user")
ch=input("\nEnter any single character from keyboard :")
if(ord(ch)>=65 and ord(ch)<=90):
    print("\n\tEnterd character is Upper Case alphabet i.e ",ch)
elif(ord(ch)>=97 and ord(ch)<=122):
    print("\n\tEnterd character is Lower Case alphabet i.e ",ch)
elif(ch==" "):
    print("\n\tEnterd character is Space")
elif(ch=="\t"):
    print("\n\tEnterd character is Tab")
elif(ch=="\'"):
    print("\n\tEnterd character is Single Quote i.e ",ch)
elif(ch=="\""):
     print("\n\tEnterd character is Double Quote i.e ",ch)
else:
     print("\n\tEnterd character is Special Character i.e ",ch)
'''elif(int(ch)>=0):
    print("\n\tEntered character is Digit i.e ",ch)'''


    
