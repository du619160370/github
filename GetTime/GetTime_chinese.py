"""Get local time and show it with chinese"""
import time

sticks = time.time()
date = time.localtime(sticks)
year = str(date.tm_year)
month = str(date.tm_mon)
day = str(date.tm_mday)
hour = str(date.tm_hour)
minute = str(date.tm_min)
second = str(date.tm_sec)
format_dict = {"0": "零", "1": "一", "2": "二", "3": "三", "4": "四", "5": "五", "6": "六", "7": "七", "8": "八", "9": "九"}

# year
year_list = [format_dict[i] for i in year]
year_ch = ""
for i in year_list:
    year_ch += i

# month
if len(month) == 1:
    month_ch = format_dict[month]
else:
    if month == "10":
        month_ch = "十"
    elif month == "11":
        month_ch = "十一"
    elif month == "12":
        month_ch = "十二"

# day
if len(day) == 1:
    day_ch = format_dict[day]
else:
    if day[0] == "1":
        if day[1] == "0":
            day_ch = "十"
        elif day[1] != "0":
            day_ch = "十"
            day_ch = day_ch + format_dict[day[1]]
    elif day[0] != "1":
        if day[1] == "0":
            day_ch = format_dict[day[0]] + "十"
        elif day[1] != "0":
            day_ch = format_dict[day[0]]
            day_ch = day_ch + "十" + format_dict[day[1]]

# hour
if len(hour) == 1:
    hour_ch = format_dict[hour]
else:
    if hour[0] == "1":
        if hout[1] == "0":
            hour_ch = "十"
        elif day[1] != "0":
            hour_ch = "十"
            hour_ch = hour_ch + format_dict[hour[1]]
    elif hour[0] != "1":
        if hour[1] == "0":
            hour_ch = format_dict[hour[0]] + "十"
        elif hour[1] != "0":
            hour_ch = format_dict[hour[0]]
            hour_ch = hour_ch + "十" + format_dict[hour[1]]

# minute
if len(minute) == 1:
    minute_ch = format_dict[minute]
else:
    if minute[0] == "1":
        if minute[1] == "0":
            minute_ch = "十"
        elif minute[1] != "0":
            minute_ch = "十"
            minute_ch += format_dict[minute[1]]
    elif minute[0] != "1":
        if minute[1] == "0":
            minute_ch = format_dict[minute[0]] + "十"
        elif minute[1] != "0":
            minute_ch = format_dict[minute[0]]
            minute_ch += "十" + format_dict[minute[1]]

# second
if len(second) == 1:
    second_ch = format_dict[second]
else:
    if second[0] == "1":
        if second[1] == "0":
            second_ch = "十"
        elif second[1] != "0":
            second_ch = "十"
            second_ch += format_dict[second[1]]
    elif second[0] != "1":
        if second[1] == "0":
            second_ch = format_dict[second[0]] + "十"
        elif second[1] != "0":
            second_ch = format_dict[second[0]]
            second_ch += "十" + format_dict[second[1]]

print("当前时间为:")
print(f"{' ' * 11}{year}.{month}.{day} {hour}:{minute}:{second}")
print(f"{' ' * 11}{year_ch}年{month_ch}月{day_ch}日 {hour_ch}时{minute_ch}分{second_ch}秒")

