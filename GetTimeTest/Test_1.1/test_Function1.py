"""
用例编号：1.1
用例标题：测试阿拉伯数字年份与月份是否成功转为汉字并正确输出
前置条件：time模块获取时间正确
输入数据：传入年份与月份(字符串)
操作步骤：
          1.分别传入阿拉伯数字年份与月份
          2.将阿拉伯数字年份与月份转换为对应汉字
          3.输出汉字年份月份与标准测试用例进行对比
预期结果：成功输出pass，失败输出fail
"""

import unittest
from Function1 import year_month

class ConvertTestCase(unittest.TestCase):
    """Test Function1.py"""

    def test1(self):
        show = year_month('2020', '1')
        self.assertEqual(show, '二零二零年一月')

    def test2(self):
        show = year_month('2020', '12')
        self.assertEqual(show, '二零二零年十二月')
    
    def test3(self):
        show = year_month('2020', '6')
        self.assertEqual(show, '二零二零年六月')

    def test4(self):
        show = year_month('9999', '1')
        self.assertEqual(show, '九九九九年一月')

    def test5(self):
        show = year_month('9999', '12')
        self.assertEqual(show, '九九九九年十二月')

    def test6(self):
        show = year_month('9999', '6')
        self.assertEqual(show, '九九九九年六月')

    def test7(self):
        show = year_month('0000', '1')
        self.assertEqual(show, '零零零零年一月')

    def test8(self):
        show = year_month('0000', '12')
        self.assertEqual(show, '零零零零年十二月')

    def test9(self):
        show = year_month('0000', '3')
        self.assertEqual(show, '零零零零年三月')

unittest.main()

