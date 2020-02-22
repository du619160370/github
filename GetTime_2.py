"""Get local time and show it"""

import time

stick = time.time()
date = time.localtime(stick)
year = date.tm_year
month = date.tm_mon
day = date.tm_mday
hour = date.tm_hour
minute = date.tm_min
second = date.tm_sec
print(f"当前时间: {year}年{month}月{day}日 {hour}:{minute}:{second}")

