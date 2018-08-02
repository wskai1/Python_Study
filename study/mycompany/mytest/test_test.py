import unittest
from unittest import TestCase

from study.mycompany.mytest.test1 import Test


class TestTest(unittest.TestCase):
    ##初始化工作
    def setUp(self):
        print("所有的测试方法都需要先执行该步骤")

    # 退出清理工作
    def tearDown(self):
        print("所有的测试方法执行完毕后都需要执行该步骤")

    def test_pri(self):
        test=Test()
        self.assertEqual(test.pri(), '这就是个普通的1测试方法', 'test  fail')
    def test_pri1(self):
        test = Test()
        self.assertEqual(test.pri1(2,3),7,'这丫没通过，和约期结果不一致')
if __name__ == '__main__':
    unittest.main()