print("Data validation for student acceptance")

data_valid = False

while data_valid == False:
    grade1 = input("Enter the grade1: ")
    try:
        grade1 =  int(grade1)
        if (grade1<0 or grade1 >10):
            print("The grade should be between 0 and 10")
            continue    
        else:
            data_valid = True
    except:
        print("Invalid")
        
data_valid = False

while data_valid == False:
    grade2 = input("Enter the grade2: ")
    try:
        grade2 =  int(grade2)
        if(grade2 < 0 or grade2 > 10):
            print("The grade should be between 0 and 10")
            continue
        else:
            data_valid = True
    except:
        print("Invalid")

data_valid = False

while data_valid == False:
    total_classes = input("Enter the total number of classes: ")
    try:
        total_classes =  int(total_classes)   
        if(total_classes < 0):
            print("The total number of classes cannot be less than 0")
            continue
        else:
            data_valid = True
    except:
        print("Invalid")

data_valid = False
while data_valid == False:
    absence = input("Enter the number of absence: ")
    try:
        absence =  int(absence)    
        if( absence < 0 or absence > total_classes):
            print("The absence cannot be less than 'o' or the total number of classes")
            continue
        else:
            data_valid = True
    except:
        print("Invalid")

avg = (grade1+grade2)/2
attendance = (total_classes-absence)/total_classes

print("The average is: ",avg)
print("The attendance of the student is: ",attendance)

if(avg > 6.5 and attendance >= 0.8):
    print("The student is eligible")
elif(avg > 6.5 and attendance <= 0.8):
    print("The student is ineligible due to shortage of attendance ")
elif(avg < 6.5 and attendance >= 0.8):
    print("The student is ineligible due to lower average")
else:
    print("Student in eligible due to shortage of both attendance and average")

