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
d1 = datetime.date(2015, 3, 11)     # only the date (note including hours, minutes, seconds)
print('d1:', d1)  # d1: 2015-03-11
d2 = d1.replace(year=1990)  # update the year; also available (month, date)
print('d2:', d2)  # d2: 1990-03-11

# Arithmetic
# We can perform arithmetic on date objects to check for time differences. For example:
d1  # datetime.date(2015, 3, 11)
d2  # datetime.date(1990, 3, 11)
d1 - d2     # datetime.timedelta(9131)
# This give us the difference in days between the two dates. You can use the timedelta method to specify various
# units of times (day,minutes,hours,etc...)
result = d1 - d2
print(result) # 9131 days, 0:00:00
result.days     # 9131


dt1 = datetime.datetime(2021, 11, 3, 22, 0)     # 2021-11-03 22:00:00
dt2 = datetime.datetime(2020, 11, 3, 12, 0)     # 2020-11-03 12:00:00
dt1 - dt2       # datetime.timedelta(days=365, seconds=36000)
3600/60/60      # 10 hours
diff = dt1 - dt2
diff.seconds    # 36000
diff.total_seconds()    # 31572000.0; total seconds = 36000 seconds + 365 days in seconds