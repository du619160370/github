import unittest
from Function3 import total_function

class ConvertTestCase(unittest.TestCase):
    """Test Function1.py"""

    def test1(self):
        show = total_function('2020', '1', '1', '1', '1', '1')
        self.assertEqual(show, '二零二零年一月一日 一点一分一秒')

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

