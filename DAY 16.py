from datetime import datetime
now = datetime.now()
print(now)
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
timestamp = now.timestamp()
print(f'{day}/{month}/{year}, {hour}:{minute}')
print('timestamp', timestamp)

now = datetime.now()
t = now.strftime("%m/%d/%Y, %H:%M:%S")
print(t)


date_string = "5 December, 2019"
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)

from datetime import date
today = date(year=2026, month=1, day=30)
new_year = date(year=2027, month=1, day=1)
time_left_for_newyear = new_year - today
print('Time left for new year: ', time_left_for_newyear)

t1 = date(year=2026, month=1, day=30)
t2 = date(year=1970, month=1, day=1)
diff = t1 - t2
print(diff)
