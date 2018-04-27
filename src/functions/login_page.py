# coding=utf-8

import time

from src.functions.public.baseaction import Baseaction
from .home_page import HomePage


class LoginPage(Baseaction):

    def login_url(self):
        return self.current_url()

    def username(self):
        return self.by_id("username")

    def password(self):
        return self.by_id("password")

    def error_msg(self):
        return self.by_class("errorMsg")

    def login_button(self):
        return self.by_id("signIn")

    def login(self, user, pwd):
        self.username().clear()
        self.username().send_keys(user)
        self.password().clear()
        self.password().send_keys(pwd)
        self.login_button().click()
        time.sleep(4)
        return HomePage(self.driver)

