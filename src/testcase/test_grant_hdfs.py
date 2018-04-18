# encoding=utf-8

import unittest
from selenium import webdriver
from src.common.initdriver import read_config
from src.functions.login_page import LoginPage
from src.functions.grant_hdfs_page import GrantHdfsPage
from config.data.policy_para import params
from parameterized import parameterized
import os
import time
class CreatePolicy(unittest.TestCase):
    """test create policy"""
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
        cls.ghp = GrantHdfsPage(cls.driver)
        cls.ghp.grant_manage().click()
        time.sleep(2)
        cls.ghp.hdfs_manger().click()
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        # pass

    def setUp(self):
        self.driver.get("http://10.2.46.93:6080/accredit.html?param=hdfs&dc=3_3dc")

    def tearDown(self):
        self.ghp.del_policy()
        time.sleep(2)
    
    @parameterized.expand(input=params)
    def test_grant(self, name, policy_name, path, desc, group, user, privilege):
        res = self.ghp.create_policy(policy_name, path, desc, group, user, privilege, sub='Y')
        self.assertEqual(res, policy_name)
        
    def test_edit(self):
        basepath = os.path.dirname(os.path.abspath(__file__))
        # print(os.path.abspath("../../config/data/login.ini"))
        config = read_config(os.path.join(basepath, "../../config/data/policy.ini"))
        policy_name = config.get("Name","name")
        path = config.get("Path","path")
        desc = config.get("Desc","desc")
        group = config.get("Group","group")
        user = config.get("User","user")
        privilege = config.get("Privilege","privilege")
        # 创建 policy
        self.ghp.create_policy("old_policy_name", "/t", "", "public", "admin", "read", sub='Y')
        time.sleep(2)
        # 修改 policy 
        res = self.ghp.edit_policy(policy_name, path, desc, group, user, privilege, sub='Y')
        self.assertEqual(res, policy_name)