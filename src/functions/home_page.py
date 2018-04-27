# coding=utf-8

from src.functions.public.baseaction import Baseaction
class HomePage(Baseaction):

    def current_user(self):
        return self.by_css("a#current_user_name")

    def modify_pwd(self, newpwd, fimpwd):
        # 点击修改密码
        self.by_id("renewPassword").click()
        # 输入新密码
        self.by_id("newpwd").send_keys(newpwd)
        # 输入确认密码
        self.by_id("fimpwd").send_keys(fimpwd)
        # 提交密码
        self.by_class(".btn.btn-submit").submit()

    def logout(self):
        self.by_id("logout").click()

