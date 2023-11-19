#HackerRank problem program for time conversion.
def time_conversion(s):
    hour = s[:2]
    minutes_seconds = s[2:]

    if ('AM' in s and hour == '12'):
        hour = '00'
        time = hour + minutes_seconds
        print(time)
    elif ('AM' in s and hour < '12'):
        time = s[:8]
        print(time)
    elif ('PM' in s and hour < '12'):
        Minutes_seconds = s[2:8]
        h = int(hour)
        Hour = h + 12
        Hour = str(Hour)
        time = Hour + Minutes_seconds
        print(time)
    elif('PM' in s and hour =='12'):
        time = s[:8]
        print(time)

s = input()
time_conversion(s)
