"""Get local time and show it"""

import time

sticks = time.time()	# time_sticks
date = time.localtime(sticks)	# changing sticks to time
# formatting date
str_date = time.strftime("%Y年%m月%d日 %H:%M:%S", date)
print(f"当前时间: {str_date}")

