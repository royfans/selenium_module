# encoding=utf-8

import unittest
from selenium import webdriver
from src.common.initdriver import read_config
from src.functions.login_page import LoginPage
from src.functions.group_manage_page import GroupManagePage
import os
import time
class CreateGroup(unittest.TestCase):
    """test create group"""
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
        gmp = GroupManagePage(cls.driver)
        gmp.auth_manage().click()
        time.sleep(2)
        gmp.group_manage().click()
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
        gmp = GroupManagePage(self.driver)
        gmp.del_group()
    def test_create_group(self):
        # 生成随机用户名
        group_name = "test_user" + str(time.time())[11:]
        group_desc = "This is the test group"
        group_num = 1
        gmp = GroupManagePage(self.driver)
        # 返回已创建的组
        res = gmp.create_group(group_name, group_desc, group_num)
        print("创建的组为：%s；列表中最后一个组为：%s。" %(res,group_name))
        time.sleep(2)

        self.assertEqual(res, group_name)

    def test_edit_group(self):
         # 生成随机用户名
        group_name = "test_user" + str(time.time())[11:]
        group_desc = "This is the test group"
        group_num = 1
        gmp = GroupManagePage(self.driver)
        # 返回已创建的组
        gmp.create_group(group_name, group_desc, group_num)
        # print("创建的组为：%s；列表中最后一个组为：%s。" %(res,group_name))
        time.sleep(2)
        new_grp_name = "test_edit_group"
        res = gmp.edit_group(new_grp_name, group_desc)
        time.sleep(2)
        self.assertEqual(new_grp_name, res)