"""
用例编号：0
用例标题：测试用户输入是否成功存入SQL数据库
前置条件：SQL数据库已运行，存在dubinDB数据库，端口号3306，编码方式utf8mb4，存在名为homework的表
输入数据：作业名称(hw_name) 时间(time) 作业详情(hw_detail) 作业进度(rate_of_process)
操作步骤：
          1.按格式传入需要写入数据库的内容
          2.程序将内容写入SQL数据库
          3.将刚写入内容读出，与输入内容进行对比是否一致
预期结果：成功输出pass，失败输出fail
"""

import unittest
from function_0 import test_function

class SQLTestCase(unittest.TestCase):
    """Test function_0.py"""

    def test1(self):
        show = test_function('test', '2020-01-01 12:12:12', 'test', 'test')
        self.assertEqual(show, 'test,2020-01-01 12:12:12,test,test')

    def test2(self):
        show = test_function('汉字测试', '1990-12-12 00:01:01', '我是汉字', '一二三四五')
        self.assertEqual(show, '汉字测试,1990-12-12 00:01:01,我是汉字,一二三四五')
    
    def test3(self):
        show = test_function('作业名称', '1995-05-05 13:13:13', '作业详情', '完成进度')
        self.assertEqual(show, '作业名称,1995-05-05 13:13:13,作业详情,完成进度')

    def test4(self):
        show = test_function('123', '1995-05-05 13:13:13', '456', '789')
        self.assertEqual(show, '123,1995-05-05 13:13:13,456,789')

unittest.main()

