# encoding=utf-8

import unittest
from selenium import webdriver
from parameterized import parameterized
from src.common.initdriver import read_config
from src.functions.login_page import LoginPage
from src.functions.home_page import HomePage
from config.data.login_err import params
import os

class Login(unittest.TestCase):
    """test login"""
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.url = "http://10.2.46.93:6080/login.jsp"
        cls.driver.get(cls.url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        # pass
    def setUp(self):
        pass
    def tearDown(self):
        pass
    # login fail test
    @parameterized.expand(input=params)
    def test_logerr(self, name, user, pwd):
        # self.driver.get(self.url)
        lp = LoginPage(self.driver)
        hp = HomePage(self.driver)
        basepath = os.path.dirname(os.path.abspath(__file__))
        print(os.path.abspath("../../config/data/login.ini"))
        config = read_config(os.path.join(basepath, "../../config/data/login.ini"))
        # user = config.get("User", "username1")
        # pwd = config.get("Password", "pwd1")
        error_msg = config.get("ErrorMsg", "msg")
        home_page = lp.login(user, pwd)
        display_msg = lp.error_msg().text.strip()
        self.assertEqual(display_msg, error_msg)

        # pass
    # test login success
    def test_login(self):

        lp = LoginPage(self.driver)
        # hp = HomePage(self.driver)
        basepath = os.path.dirname(os.path.abspath(__file__))
        # print(os.path.abspath("../../config/data/login.ini"))
        config = read_config(os.path.join(basepath, "../../config/data/login.ini"))
        user = config.get("User", "username1")
        pwd = config.get("Password", "pwd1")

        home_page = lp.login(user, pwd)
        print("---------------------")
        print(home_page.current_user().text)
        self.assertIn(user,home_page.current_user().text)


    def test_logout(self):
        HomePage(self.driver).logout()
        self.assertEqual(self.driver.current_url,self.url)



if __name__ == "__main__":

    unittest.main(verbosity=2)
