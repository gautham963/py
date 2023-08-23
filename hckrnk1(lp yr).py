def is_leap(year):
    leap = False
    if year < 0:
        print(False)
        if (year%4) == 0:
            if (year%4)== 0 and (year%100) == 0:
                print(False)
            elif (year%4) == 0 and (year%400) == 0:
               return leap 
        return leap

year = int(input())
print(is_leap(year))
