import math
print("This program calculates the area and circumference of the circle")
pi = math.pi
radius = float(input("Enter the radius of the circle"))
print("The area of the circle is",round(pi*(radius*radius),4))
print("The circumference of the circle is",round(2*pi*radius,4))
