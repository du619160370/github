import unittest
from Function1 import year_month

class ConvertTestCase(unittest.TestCase):
    """Test Function1.py"""

    def test1(self):
        show = year_month('2020', '1')
        self.assertEqual(show, '二零二零年一月')

    def test2(self):
        show = year_month('2020', '11')
        self.assertEqual(show, '二零二零年十一月')
    def test3(self):
        show = year_month('1999', '2')
        self.assertEqual(show, '一九九九年二月')

    def test4(self):
        show = year_month('1999', '12')
        self.assertEqual(show, '一九九九年十二月')

unittest.main()

