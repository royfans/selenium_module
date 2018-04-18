# coding = utf-8

import unittest, time, re
import HTMLTestRunner
import os
def all_test():
    basepath = os.path.dirname(os.path.abspath(__file__))

    test_dir = os.path.join(basepath, "\\..\\testcase")
    discover = unittest.defaultTestLoader.discover(
        test_dir,
        pattern='test_*.py',
        top_level_dir=None)
    # 定义测试报告
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    filename = basepath + "\\..\\..\\report\\" + now + '\\result.html'
    fq = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fq,
        title='雷池综合管理系统测试报告',
        description='登录、创建用户和组、授权相关功能测试报告')
    # runner = unittest.TextTestRunner()
    runner.run(discover)
    fq.close()

if __name__ == '__main__':
    all_test()