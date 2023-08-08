print('This program calculates the Body Mass Index(BMI)')
h = float(input("Enter your height in meters: "))
w = float(input("Enter your weight in kilograms: "))

bmi = w/(h*h)
print(round(bmi,1))

if(bmi <= 18.5):
    print("Underweight")
if(bmi >18.5 and bmi <= 24.9):
    print("Normal weight")
if(bmi > 24.9 and bmi <= 29.9):
    print("Overweight")
else:
    print("Obesity")
    

          
