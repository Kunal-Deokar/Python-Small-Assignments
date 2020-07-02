#to find Area ,circumference, volume of cylinder
print("Calculate Area,Circumference and Volume of Cylinder here")
rad=int(input("\nEnter the radius of Cylinder :"))
height=int(input("\nEnter the height of Cylinder :"))
print("\n\tTotal Surface Area of Cylinder = ",(2*3.14*rad*(rad+height)))
print("\n\tCross Section Area of Cylinder = ",3.14*rad**2)
print("\n\tVolume of Cylinder = ",3.14*(rad**2)*height)
