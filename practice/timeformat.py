from datetime import datetime

# current dateTime
now = datetime.now()

# convert to string
date_time_str = now.strftime("%Y-%m-%d %H:%M:%S")
print('DateTime String:', date_time_str)

# Output 2021-07-20 16:26:24

# convert to date String
date = now.strftime("%d/%m/%Y")
print('Date String:', date)

# convert to time String
time = now.strftime("%H:%M:%S")
print('Time String:', time)

# year
year = now.strftime("%Y")
print('Year String:', year)

# Month
month = now.strftime("%m")
print('Month String:', month)

# Day
day = now.strftime("%d")
print('Day String:', day)
