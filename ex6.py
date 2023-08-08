print("This take's the users birth date and gives the month")
month = ("January", "Febraury" , "March" , "April" , "May" , "June" , "July" , "August" , "September" , "October" , "November" , "December")

date = input("Enter your birthday in'DD-MM-YYYY' format")
bd_date = int(date[3:5])-1
bd_month = month[bd_date]

print("your birthday month is: ",bd_month)
