import calendar

def dayFinder(date):

    day, month, year  = (int(i) for i in date.split(' '))
    daynumber = calendar.weekday(year, month, day)

    days = ['Monday','Tuesday','Wednesday','Tuesday','Friday','Saturday','Sunday']

    Day = days[daynumber]

    Day.upper()

    return Day

date = input()

print(dayFinder(date))
