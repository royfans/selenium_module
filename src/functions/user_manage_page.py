# coding=utf-8

from .baseaction import Baseaction
import time
class UserMangePage(Baseaction):

    # 定位认证管理
    def auth_manage(self):
        return self.by_text(u"认证管理")
    # 定位用户管理
    def user_manage(self):
        return self.by_text(u"用户管理")
    # 定位创建按钮
    def add_user(self):
        return self.by_id("addUser-click")

    # 定位所使用编辑按钮，返回列表
    def edit_btm(self):
        return self.by_all_css("button.btn.btn-submit.editUser-click")

    # 定位删除按钮
    def del_btm(self):
        return self.by_all_css("#del-click")

    # 定位删除弹出框【确认删除】按钮
    def del_yes(self):
        return self.by_css("a.layui-layer-btn0")

    # 定位删除弹出框【取消】按钮
    def del_no(self):
        return self.by_css("a.layui-layer-btn1")
    # 定位下载按钮
    def download_btm(self):
        return self.by_all_css("tr > td > a")
    # 定位用户名
    def user_name(self):
        return self.by_id("textname")
    # 定位选择创建密码登录用户
    def select_password(self):
        return self.by_css("div:nth-child(2) > span")
    # keytab 用户
    def select_keytab(self):
        return self.by_css("#addUserform > div.layui-form-item.layui-input-block.app_group_for > div.layui-unselect.layui-form-radio.layui-form-radioed > span")
    # 应用名
    def input_app(self):
        return self.by_id("input_app")
    # 输入密码
    def input_pwd(self):
        return self.by_id("input_password")
    # 输入确认密码
    def input_pwd_solve(self):
        return self.by_id("passwd_solve")
    # 定位组
    def group(self):
        return self.by_css(".select2-search__field")
    # 提交按钮
    def submit(self):
        return self.by_id("add_user")

    # 获取用户名,做断言使用
    def user_list(self):
        return self.by_all_css("tr > td.name")

    # 获取应用名，做断言使用
    def app_list(self):
        return self.by_all_css("tr > td:nth-child(3)")

    # 创建 keytab 用户
    def create_keytab_user(self, user_name, app_name, group_name):
        # self.auth_manage().click()
        # self.user_manage().click()
        self.add_user().click()
        self.user_name().send_keys(user_name)
        self.input_app().send_keys(app_name)
        # self.group().send_keys(group_name)
        self.submit().click()
        time.sleep(2)
        # print(self.user_list()[-1].text)
        return self.user_list()[-1].text

    # 创建 pwd 用户
    def create_pwd_user(self, user_name, password, group_name):
        # self.auth_manage().click()
        # self.user_manage().click()
        time.sleep(2)
        self.add_user().click()
        self.user_name().send_keys(user_name)
        self.select_password().click()
        self.input_pwd().send_keys(password)
        self.input_pwd_solve().send_keys(password)
        # self.group().send_keys(group_name)
        self.submit().click()
        time.sleep(2)
        return self.user_list()[-1].text

    def edit_user(self, app_name):
        self.edit_btm()[-1].click()
        self.input_app().clear()
        self.input_app().send_keys(app_name)
        self.submit().click()
        time.sleep(2)
        # 返回编辑后的应用名
        return self.app_list()[-1].text

    def del_user(self):
        self.del_btm()[-1].click()
        self.del_yes().click()
        # 返回删除用户后，用户列表中的最后一个用户的用户名
        return self.user_list()[-1].text






