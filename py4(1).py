marks1 = float(input("Enter the marks of the first test: "))
marks2 = float(input("Enter the marks of the second test: "))
absent = int(input("Enter the number of days absent: "))
total_days = int(input("Enter the number of days: "))

avg  = (marks1 + marks2)/2
attendance = (total_days - absent)/total_days

print("The average grade: ",avg)
print("The attendance rate: ",str(round((attendance*100),3))+'%')

if(avg > 7.5 and attendance > 0.8):
     print("Student is elligible")
elif(avg < 7.5 and attendance < 0.8):
     print("The student has failed due to lower attendance as well as lower avg")
elif(avg > 7.5 and attendance < 0.8):
    print("The student is inelligible due to shortage of atendance[critera 80%]")
else:
    print("The student is inelligible due to avg grade less than 7.5")
