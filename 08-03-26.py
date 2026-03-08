#India won T20 world Cup today 

# DATE AND TIME
import datetime
import pytz

# to pass date in Year-Month-date without zeros in prefix
day = datetime.date(2024,7,23)
print(day)

#  to print today's date
tday = datetime.date.today()
print(tday)
# we can also use grape today month year day
print(tday.year)
print(tday.month)
print(tday.day) 
print(tday.weekday())# 0 is Monday 6 is sunday
print(tday.isoweekday()) # 1 is Monday 7 is sunday

# Time Deltas
# diff within days check what will be date after 7 days

tdeltas = datetime.timedelta(days=7)
print(tday + tdeltas) ## add sign means date after 7 days 
print(tday - tdeltas) # sub sign means date before 7 days

# print(tday - tdelta)
# date2 = date 1 + timedelta
# timedelta = date1 + date2

bday = datetime.date(2026,11,5)
till_bday = bday - tday
print(till_bday.days)



###############################################

# TIME

# create new time using datetime function
t = datetime.time(1,2,45,100000)
print(t)
print(t.hour)

# create new datetime with datetime all of it

dt = datetime.datetime(2000,11,5,19,58,45,100000)
tdeltas = datetime.timedelta(days=7)
print(dt.date())
print(dt.time())
print(dt.year)
print(dt + tdeltas)

dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()
print(dt_today)
print(dt_now)
print(dt_utcnow)

dt = datetime.datetime(2026,3,9,1,25,30,tzinfo=pytz.UTC)
print(dt)
