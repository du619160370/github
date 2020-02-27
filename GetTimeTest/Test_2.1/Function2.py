"""Get local time and show it with chinese"""
import time

def day_hour_minute_second(day, hour, minute, second):
    format_dict = {"0": "零", "1": "一", "2": "二", "3": "三", "4": "四", "5": "五", "6": "六", "7": "七", "8": "八", "9": "九"}
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
    show = f"{day_ch}日 {hour_ch}点{minute_ch}分{second_ch}秒"

    return show

