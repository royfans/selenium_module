# coding=utf-8

from src.testcase.test_login import Login
from src.testcase.test_create_group import CreateGroup
from src.testcase.test_create_user import CreateUser
from src.testcase.test_grant_hdfs import CreatePolicy
import unittest
# 添加一个测试集合，并添加 Case

# 登录测试用例集合--暂不用
def suite():
    suiteTest = unittest.TestSuite()
    suiteTest.addTest(Login('test_logerr'))
    # suiteTest.addTest(Login('test_login'))
    # suiteTest.addTest(Login('test_logout'))
    return suiteTest
# 登录测试用例集--带参数化
def suite1():
    suit = unittest.TestLoader().discover("src/testcase/", pattern="test_login.py", top_level_dir=None)
    # runner = unittest.TextTestRunner()
    # runner.run(suit)
    return suit
# 创建用户测试用例集
def suite2():
    suiteTest = unittest.TestSuite()
    suiteTest.addTest(CreateUser('test_create_keytab_user'))
    suiteTest.addTest(CreateUser('test_create_pwd_user'))
    suiteTest.addTest(CreateUser('test_edit'))

    return suiteTest
# 创建组用例集
def suite3():
    suiteTest = unittest.TestSuite()
    # suiteTest.addTest(CreateGroup('test_create_group'))
    suiteTest.addTest(CreateGroup('test_edit_group'))
    return suiteTest

# 创建policy用例集
def suite4():
    # suiteTest = unittest.TestSuite()
    # suiteTest.addTest(CreatePolicy('test_grant'))
    suit = unittest.TestLoader().discover("src/testcase/", pattern="test_grant_hdfs.py", top_level_dir=None)   
    return  suit

# 包含所有的Suite
def all_suite():
    allTest = unittest.TestSuite((suite2()))
    return allTest

# 指定并启动测试集合，运行集合方法
if __name__ == "__main__":

    runner = unittest.TextTestRunner()
    runner.run(suite2())