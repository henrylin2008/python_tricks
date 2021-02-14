# datetime
# Python has the datetime module to help deal with timestamps in your code. Time values are represented with the time
# class. Times have attributes for hour, minute, second, and microsecond. They can also include time zone information.
# The arguments to initialize a time instance are optional, but the default of 0 is unlikely to be what you want.
#
# time
# Lets take a look at how we can extract time information from the datetime module. We can create a time-stamp by
# specifying datetime.time(hour,minute,second,microsecond)

import datetime

t = datetime.time(4, 20, 1)  # time(hour[, minute[, second[, microsecond[, tzinfo]]]])
# Lets show the different components

print(t)  # 04:20:01
print('hour  :', t.hour)  # hour: 4
print('minute:', t.minute)  # minute: 20
print('second:', t.second)  # second: 1
print('microsecond:', t.microsecond)  # microsecond: 0
print('tzinfo:', t.tzinfo)  # tzinfo: None
# Note: A time instance only holds values of time, and not a date associated with the time.

# We can also check the min and max values a time of day can have in the module:
print('Earliest:', datetime.time.min)  # Earliest: 00:00:00
print('Latest:', datetime.time.max)  # Latest: 23:59:59.999999
print('Resolution:', datetime.time.resolution)  # Resolution: 0:00:00.000001
# The min and max class attributes reflect the valid range of times in a single day.


# Dates
# datetime (as you might suspect) also allows us to work with date timestamps. Calendar date values are represented with
# the date class. Instances have attributes for year, month, and day. It is easy to create a date representing today’s
# date using the today() class method.
# from datetime import datetime

today = datetime.date.today()
print(today)  # 2021-01-18
print('ctime:', today.ctime())  # 'Mon Jan 18 00:00:00 2021'
print('tuple:', today.timetuple())
# time.struct_time(tm_year=2021, tm_mon=1, tm_mday=18, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=0, tm_yday=18,
#                  tm_isdst=-1)
print('ordinal:', today.toordinal())  # ordinal: 737808
print('Year:', today.year)  # Year: 2021
print('Mon :', today.month)  # Mon: 1
print('Day :', today.day)  # Day: 18

# As with time, the range of date values supported can be determined using the min and max attributes.
print('Earliest  :', datetime.date.min)  # Earliest  : 0001-01-01
print('Latest    :', datetime.date.max)  # Latest    : 9999-12-31
print('Resolution:', datetime.date.resolution)  # Resolution: 1 day, 0:00:00

# Another way to create new date instances uses the replace() method of an existing date. For example, you can change
# the year, leaving the day and month alone
d1 = datetime.date(2015, 3, 11)  # only the date (note including hours, minutes, seconds)
print('d1:', d1)  # d1: 2015-03-11
d2 = d1.replace(year=1990)  # update the year; also available (month, date)
print('d2:', d2)  # d2: 1990-03-11

# Arithmetic
# We can perform arithmetic on date objects to check for time differences. For example:
d1  # datetime.date(2015, 3, 11)
d2  # datetime.date(1990, 3, 11)
d1 - d2  # datetime.timedelta(9131)
# This give us the difference in days between the two dates. You can use the timedelta method to specify various
# units of times (day,minutes,hours,etc...)
result = d1 - d2
print(result)  # 9131 days, 0:00:00
result.days  # 9131

dt1 = datetime.datetime(2021, 11, 3, 22, 0)  # 2021-11-03 22:00:00
dt2 = datetime.datetime(2020, 11, 3, 12, 0)  # 2020-11-03 12:00:00
dt1 - dt2  # datetime.timedelta(days=365, seconds=36000)
3600 / 60 / 60  # 10 (hours)
diff = dt1 - dt2
diff.seconds  # 36000
diff.total_seconds()  # 31572000.0; total seconds = 36000 seconds + 365 days in seconds

# get Current Date and Time
import datetime

now = datetime.datetime.now()  # get current local date and time
print(now)  # 2021-01-18 10:39:29.835696

current_time = datetime.datetime.now().time()
# 10:39:29.835696

today = datetime.date.today()  # get current date
print(today)  # 2021-10-18

d = datetime.date(2020, 4, 13)  # set a date
print(d)  # 2020-04-13

# get current date
from datetime import date

# date object of today's date
today = date.today()

print("Current year:", today.year)  # 2021
print("Current month:", today.month)  # 01
print("Current day:", today.day)  # 18

# time object to represent time
from datetime import time

# time(hour = 0, minute = 0, second = 0)
a = time()
print("a =", a)  # a = 00:00:00

# time(hour, minute and second)
b = time(11, 34, 56)
print("b =", b)  # b = 11:34:56

# time(hour, minute and second)
c = time(hour=11, minute=34, second=56)
print("c =", c)  # c = 11:34:56

# time(hour, minute, second, microsecond)
d = time(11, 34, 56, 234566)
print("d =", d)  # d = 11:34:56.234566

# difference between two dates and times
from datetime import date, datetime

t1 = date(2018, 7, 12)
t2 = date(2017, 12, 23)
t3 = t1 - t2
print(t3)  # 201 days, 0:00:00

t4 = datetime(2018, 7, 12, 7, 9, 33)
t5 = datetime(2019, 6, 10, 5, 55, 13)
print(t4 - t5)  # -333 days, 1:14:20

# difference between two timedelta objects

from datetime import timedelta

t1 = timedelta(weeks=2, days=5, hours=1, seconds=33)
t2 = timedelta(days=4, hours=11, minutes=4, seconds=54)
t3 = t1 - t2

print("t3 =", t3)  # t3 = 14 days, 13:55:39

# negative timedelta object
from datetime import timedelta

t1 = timedelta(seconds=33)
t2 = timedelta(seconds=54)
t3 = t1 - t2
print("t3 =", t3)  # t3 = -1 day, 23:59:39
print("t3 =", abs(t3))  # t3 = 0:00:21

t = timedelta(days=5, hours=1, seconds=33, microseconds=233423)
print("total seconds =", t.total_seconds())  # total seconds = 435633.233423


# Time module
import time

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
print(current_time) # 07:46:58

# time.sleep(): suspends/delays execution of the current thread for given # of seconds
print("This is printed immediately.")
time.sleep(2.4)
print("This is printed after 2.4 seconds.")

named_tuple = time.localtime() # get struct_time
time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)

print(time_string)  # 12/28/2018, 09:47:41


# Format Datetime

# strftime() creates a formatted string from a given date, datetime, or time object
now = datetime.now()    # 2021-01-18 11:14:00.271193
t = now.strftime("%m/%d/%Y, %H:%M:%S")  # 01/18/2021, 11:14:00
# %Y  - year as a decimal num [0001,..., 2018, 2019,..., 9999]
# %m  - month as a zero-padded decimal number [01, 02, ..., 11, 12]
# %d  - day as a zero-padded decimal [01, 02, ..., 30, 31]
# %H  - hour as a zero-padded decimal [00, 01, ..., 22, 23]
# %M  - minute [00, 01,     ..., 58, 59]
# %S  - second [00, 01, ..., 58, 59]
# %a  - abbreviated weekday name [Sun,Mon,...]
# %A  - Full weekday name [Sunday, Monday, ..]
# %w  - weekday as a decimal number [0,1,..,6]
# %-d - day as a decimal number [1,2,.....,30]
# %b  - Abbreviated month name  [Jan,Feb,..,Dec]
# %B  - Full month name [January, February,..]
# %-m - Month as a decimal number [1,2,...,12]
# %y  - Year as a zero-padded decimal number [00,01,...99]
# %-H - Hour (24-hour) as a decimal number [0,1,...23]
# %I  - Hour (12-hour) as a zero-padded decimal number [01,02...12]
# %-I - Hour (12-hour) as a decimal num [1,2,...12]
# %p  -	Locale’s AM or PM.	[AM, PM]
# %M  - Minute as a zero-padded decimal number.	[00, 01, ..., 59]
# %-M - Minute as a decimal number.	[0, 1, ..., 59]
# %S  - Second as a zero-padded decimal number.	[00, 01, ..., 59]
# %-S - Second as a decimal number.	[0, 1, ..., 59]
# %f  - Microsecond as a decimal number, zero-padded on the left.	[000000 - 999999]
# %z  - UTC offset in the form +HHMM or -HHMM.
# %Z  -	Time zone name.
# %j  -	Day of the year as a zero-padded decimal number. [001, 002, ..., 366]
# %-j -	Day of the year as a decimal number.	[1, 2, ..., 366]
# %U  -	Week number of the year (Sunday as the first day of the week). All days in a new year preceding the first Sunday
#       are considered to be in week 0.	[00, 01, ..., 53]
# %W  - Week number of the year (Monday as the first day of the week). All days in a new year preceding the first Monday
#       are considered to be in week 0.	[00, 01, ..., 53]
# %c  -	Locale’s appropriate date and time representation.	[Mon Sep 30 07:06:05 2013]
# %x  - Locale’s appropriate date representation.	[09/30/13]
# %X  - Locale’s appropriate time representation.	[07:06:05]
# %%  -	A literal '%' character.	[%]



# The strptime() method creates a datetime object from a given string (representing date and time).
# The strptime() class method takes two arguments:
#   -string (that be converted to datetime)
#   -format code
date_string = "21 June, 2018, 10:30:00"     # 21 June, 2018, 10:30:00
date_object = datetime.strptime(date_string, "%d %B, %Y, %H:%M:%S")
# %d, %B and %Y format codes are used for day, month(full name) and year respectively.
print(date_object)  # 2018-06-21 10:30:00
# %a	Abbreviated weekday name.	Sun, Mon, ...
# %A	Full weekday name.	Sunday, Monday, ...
# %w	Weekday as a decimal number.	0, 1, ..., 6
# %d	Day of the month as a zero-padded decimal.	01, 02, ..., 31
# %-d	Day of the month as a decimal number.	1, 2, ..., 30
# %b	Abbreviated month name.	Jan, Feb, ..., Dec
# %B	Full month name.	January, February, ...
# %m	Month as a zero-padded decimal number.	01, 02, ..., 12
# %-m	Month as a decimal number.	1, 2, ..., 12
# %y	Year without century as a zero-padded decimal number.	00, 01, ..., 99
# %-y	Year without century as a decimal number.	0, 1, ..., 99
# %Y	Year with century as a decimal number.	2013, 2019 etc.
# %H	Hour (24-hour clock) as a zero-padded decimal number.	00, 01, ..., 23
# %-H	Hour (24-hour clock) as a decimal number.	0, 1, ..., 23
# %I	Hour (12-hour clock) as a zero-padded decimal number.	01, 02, ..., 12
# %-I	Hour (12-hour clock) as a decimal number.	1, 2, ... 12
# %p	Locale’s AM or PM.	AM, PM
# %M	Minute as a zero-padded decimal number.	00, 01, ..., 59
# %-M	Minute as a decimal number.	0, 1, ..., 59
# %S	Second as a zero-padded decimal number.	00, 01, ..., 59
# %-S	Second as a decimal number.	0, 1, ..., 59
# %f	Microsecond as a decimal number, zero-padded on the left.	000000 - 999999
# %z	UTC offset in the form +HHMM or -HHMM.
# %Z	Time zone name.
# %j	Day of the year as a zero-padded decimal number.	001, 002, ..., 366
# %-j	Day of the year as a decimal number.	1, 2, ..., 366
# %U	Week number of the year (Sunday as the first day of the week). All days in a new year preceding the first Sunday
#       are considered to be in week 0.	00, 01, ..., 53
# %W	Week number of the year (Monday as the first day of the week). All days in a new year preceding the first Monday
#       are considered to be in week 0.	00, 01, ..., 53
# %c	Locale’s appropriate date and time representation.	Mon Sep 30 07:06:05 2013
# %x	Locale’s appropriate date representation.	09/30/13
# %X	Locale’s appropriate time representation.	07:06:05
# %%	A literal '%' character.	%

# Timezone
# use 3rd-party pytZ module
import pytz

tz_Pacific = pytz.timezone('US/Pacific')    # pytz time zones
# https://gist.github.com/heyalexej/8bf688fd67d7199be4a1682b3eec7568
datetime_Pacific = datetime.now(tz_Pacific)     # 2021-01-18 11:57:06.890240-08:00
print(datetime_Pacific.strftime("%m/%d/%Y, %H:%M:%S"))  # 01/18/2021, 11:57:06
