# coding = utf-8

import unittest, time, re
# import HTMLTestRunner
from src.runner import all_suite
from src.runner import all_suite2
if __name__ == '__main__':

    runner = unittest.TextTestRunner()
    # 调试用
    # runner.run(all_suite2.all_suite())
    # 正式测试生成测试报告用
    runner.run(all_suite.all_test())

    """
    # 执行全部测试用例
    suit = unittest.TestLoader().discover("src/testcase",pattern="test*.py",top_level_dir=None)
     runner = unittest.TextTestRunner()
     runner.run(suit)
    """
