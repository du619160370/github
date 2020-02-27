"""
用例编号：3.1
用例标题：测试阿拉伯数字年,月,日,时,分,秒是否成功转为汉字并正确输出
前置条件：time模块获取时间正确
输入数据：传入年,月,日,时,分,秒(字符串)
操作步骤：
          1.分别传入阿拉伯数字
          2.将阿拉伯数字转换为对应汉字
          3.输出汉字”xxxx年x月x日 x点x分x秒“与标准测试用例进行对比
预期结果：成功输出pass，失败输出fail
"""

import unittest
from Function3 import total_function

class ConvertTestCase(unittest.TestCase):
    """Test Function3.py"""

    def test1(self):
        show = total_function('0000', '1', '1', '0', '0', '0')
        self.assertEqual(show, '零零零零年一月一日 零点零分零秒')

    def test2(self):
        show = total_function('2010', '10', '10', '10', '10', '10')
        self.assertEqual(show, '二零一零年十月十日 十点十分十秒')
    def test3(self):
        show = total_function('2011', '11', '11', '11', '11', '11')
        self.assertEqual(show, '二零一一年十一月十一日 十一点十一分十一秒')

    def test4(self):
        show = total_function('2020', '3', '20', '20', '20', '20')
        self.assertEqual(show, '二零二零年三月二十日 二十点二十分二十秒')
    def test5(self):
        show = total_function('1923', '9', '23', '23', '59', '59')
        self.assertEqual(show, '一九二三年九月二十三日 二十三点五十九分五十九秒')

unittest.main()

