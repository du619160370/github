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

# day,hour,minute,second
def form_change(time1):
    """Change Arabic numberals to Chinese"""

    if len(time1) == 1:
        time_ch = format_dict[time1]
    else:
        if time1[0] == "1":
            if time1[1] == "0": 
                time_ch = "十"
            elif time1[1] != "0":
                time_ch = "十"
                time_ch += format_dict[time1[1]]
        elif time1[0] != "1":
            if time1[1] == "0":
                time_ch = format_dict[time1[0]] + "十"
            elif time1[1] != "0":
                time_ch = format_dict[time1[0]]
                time_ch += "十" + format_dict[time1[1]]
    return time_ch

day_ch = form_change(day)
hour_ch = form_change(hour)
minute_ch = form_change(minute)
second_ch = form_change(second)

print("当前时间为:")
print(f"{' ' * 11}{year}.{month}.{day} {hour}:{minute}:{second}")
print(f"{' ' * 11}{year_ch}年{month_ch}月{day_ch}日 {hour_ch}点{minute_ch}分{second_ch}秒")

