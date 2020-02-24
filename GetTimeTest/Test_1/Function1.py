"""Test for year and  month"""

import time

def year_month(year, month):
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
    
    result = year_ch + "年" + month_ch + "月"
    return result

