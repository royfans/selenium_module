# encoding=utf-8

import unittest
from selenium import webdriver
from src.common.initdriver import read_config
from src.functions.login_page import LoginPage
from src.functions.user_manage_page import UserMangePage

import os
import time
class CreateUser(unittest.TestCase):
    """test create user"""
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.url = "http://10.2.46.93:6080/login.jsp"
        cls.driver.get(cls.url)

        lp = LoginPage(cls.driver)
        # hp = HomePage(self.driver)
        basepath = os.path.dirname(os.path.abspath(__file__))
        # print(os.path.abspath("../../config/data/login.ini"))
        config = read_config(os.path.join(basepath, "../../config/data/login.ini"))
        user = config.get("User", "username1")
        pwd = config.get("Password", "pwd1")
        lp.login(user, pwd)
        time.sleep(2)
        ump = UserMangePage(cls.driver)
        ump.auth_manage().click()
        ump.user_manage().click()
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        # pass
    def setUp(self):
        # 恢复到最初的界面
        # self.driver.get("http://10.2.46.93:6080/index.html")
        # pass
        time.sleep(1)
    def tearDown(self):
        # 清理环境
        time.sleep(2)
        ump = UserMangePage(self.driver)
        ump.del_user()
    def test_create_keytab_user(self):
        # 生成随机用户名
        user_name = "test_user" + str(time.time())[11:]
        app_name = "hdfsdev"
        group_name = ""
        ump = UserMangePage(self.driver)
        # 返回已创建的用户
        res = ump.create_keytab_user(user_name, app_name, group_name)
        print("创建的用户为：%s；列表中最后一个用户为：%s。" %(res,user_name))
        time.sleep(2)

        self.assertEqual(res, user_name)
    def test_create_pwd_user(self):
        # 生成随机用户名
        user_name = "test_user" + str(time.time())[11:]
        # 用户密码
        password = "test123456"
        # 所选组
        group_name = ""
        time.sleep(1)
        ump = UserMangePage(self.driver)
        res = ump.create_pwd_user(user_name, password, group_name)
        print("创建的用户为：%s；列表中最后一个用户为：%s。" %(res, user_name) )
        self.driver.implicitly_wait(2)
        self.assertEqual(res, user_name)
    def test_edit(self):
        # 生成随机用户名
        user_name = "test_user" + str(time.time())[11:]
        app_name = "hdfsdev"
        app_name_fixd = "hadoopdev"
        group_name = ""
        ump = UserMangePage(self.driver)
        # 返回已创建的用户
        res = ump.create_keytab_user(user_name, app_name, group_name)
        print("创建的用户为：%s；列表中最后一个用户为：%s。" % (res, user_name))
        res = ump.edit_user(app_name_fixd)
        print("修改后的应用名为：%s" %res)
        self.driver.implicitly_wait(3)
        self.assertEqual(res, app_name_fixd)












if __name__ == "__main__":

    unittest.main(verbosity=2)