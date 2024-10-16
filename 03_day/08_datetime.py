from datetime import datetime, date, time

current_datetime = datetime.now()
print(current_datetime)
print(current_datetime.year)
print(current_datetime.month)
print(current_datetime.day)
print(current_datetime.hour)
print(current_datetime.minute)
print(current_datetime.second)
print(current_datetime.microsecond)

my_date = datetime(2021, 1, 1)
print(my_date)
print(my_date.isoformat())
print(my_date.strftime("%Y. %B %d."))
print(datetime(2021, 12, 14, 10, 10, 10) - datetime(2021, 1, 1, 5, 5, 5))
date_diff = datetime(2021, 12, 14, 10, 10, 10) - datetime(2021, 1, 1, 5, 5, 5)
print(date_diff.days)
print(date_diff.seconds / 3600)

d = date(2021, 1, 1)
t = time(10, 10, 10)
print(d)
print(t)
print(datetime.combine(d, t))
