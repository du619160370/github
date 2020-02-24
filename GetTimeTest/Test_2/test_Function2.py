import unittest
from Function2 import day_hour_minute_second

class ConvertTestCase(unittest.TestCase):
    """Test Function1.py"""

    def test1(self):
        show = day_hour_minute_second('12', '12', '12', '12')
        self.assertEqual(show, '十二日 十二点十二分十二秒')

    def test2(self):
        show = day_hour_minute_second('1', '1', '1', '1')
        self.assertEqual(show, '一日 一点一分一秒')
    def test3(self):
        show = day_hour_minute_second('10', '10', '10', '10')
        self.assertEqual(show, '十日 十点十分十秒')

    def test4(self):
        show = day_hour_minute_second('20', '20', '20', '20')
        self.assertEqual(show, '二十日 二十点二十分二十秒')
    
    def test5(self):
        show = day_hour_minute_second('23', '23', '23', '23')
        self.assertEqual(show, '二十三日 二十三点二十三分二十三秒')

unittest.main()

