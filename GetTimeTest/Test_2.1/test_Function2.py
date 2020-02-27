"""
用例编号：2.1
用例标题：测试阿拉伯数字天，时，分钟，秒是否成功转为汉字并正确输出
前置条件：time模块获取时间正确
输入数据：传入天，时，分钟，秒(字符串)
操作步骤：
          1.分别传入阿拉伯数字
          2.将阿拉伯数字转换为对应汉字
          3.输出汉字天，时，分钟，秒与标准测试用例进行对比
预期结果：成功输出pass，失败输出fail
"""

import unittest
from Function2 import day_hour_minute_second

class ConvertTestCase(unittest.TestCase):
    """Test Function2.py"""

    def test1(self):
        show = day_hour_minute_second('1', '0', '0', '0')
        self.assertEqual(show, '一日 零点零分零秒')

    def test2(self):
        show = day_hour_minute_second('31', '0', '0', '0')
        self.assertEqual(show, '三十一日 零点零分零秒')

    def test3(self):
        show = day_hour_minute_second('11', '0', '0', '0')
        self.assertEqual(show, '十一日 零点零分零秒')

    def test4(self):
        show = day_hour_minute_second('11', '24', '0', '0')
        self.assertEqual(show, '十一日 二十四点零分零秒')
    
    def test5(self):
        show = day_hour_minute_second('11', '13', '0', '0')
        self.assertEqual(show, '十一日 十三点零分零秒')

    def test6(self):
        show = day_hour_minute_second('11', '13', '59', '0')
        self.assertEqual(show, '十一日 十三点五十九分零秒')
    
    def test7(self):
        show = day_hour_minute_second('11', '13', '12', '0')
        self.assertEqual(show, '十一日 十三点十二分零秒')

    def test8(self):
        show = day_hour_minute_second('11', '13', '12', '59')
        self.assertEqual(show, '十一日 十三点十二分五十九秒')

    def test9(self):
        show = day_hour_minute_second('11', '13', '12', '25')
        self.assertEqual(show, '十一日 十三点十二分二十五秒')

unittest.main()

