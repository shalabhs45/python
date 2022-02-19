from datetime import datetime, time

now = datetime.now()

print('Current DateTime:', now)
print('Type:', type(now))


current_date = now.date()
print('Date:', current_date)
print(type(current_date))

current_time = now.time()
print('Time', current_time)
print(type(current_time))

print("Year:", now.year)
print("Month:", now.month)
print("Day =", now.day)

print("Hour:", now.hour)
print("Minute:", now.minute)
print("Second:", now.second)
print("Microsecond:", now.microsecond)

from datetime import date

today = date.today()
print('Current Date:', today)

# Output 2021-07-16


