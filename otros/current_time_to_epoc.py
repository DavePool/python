from datetime import datetime,time
import time 


def calculte_time(days_to_calculate):

    current_time = time.time()
    days = days_to_calculate
    past_days_time = (current_time - (days * 86400))

    # 23.59 hrs
    day_in_seconds = "86399"

    now = datetime.now().strftime("%H:%M:%S")
  
    now_timetuple = datetime.strptime(now, '%H:%M:%S')

    clean_time = now_timetuple - datetime(1900,1,1)
    seconds = clean_time.total_seconds()

    diff_hours = float(day_in_seconds) - seconds

    fix_hour = past_days_time + diff_hours


    date_time_obj = datetime.fromtimestamp(fix_hour).strftime('%Y-%m-%dT%H:%M:%SZ')
    return date_time_obj

now = datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
print(f"The time is {now}")

# print(calculte_time(15))