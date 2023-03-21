from datetime import datetime,time, timedelta
import time
# 2022-06-30T19:42:05Z
# convert UTC time to Mexico UTC-5
diference = 18000

utc = datetime.strptime('2022-06-30T19:42:05Z', '%Y-%m-%dT%H:%M:%SZ')


#convert into timetuple the values
utc_tuple = utc.timetuple()

print(utc_tuple)

utc_timestamp = time.mktime(utc_tuple)

print(type(utc_timestamp))

converted = utc_timestamp - diference

print(converted)

date_time_obj = datetime.fromtimestamp(converted).strftime('%Y-%m-%d %H:%M:%S')

print(date_time_obj)