# coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from .baseaction import Baseaction
from .home_page import HomePage
import time
import random
class GrantHdfsPage(Baseaction):

    # 定位授权管理
    def grant_manage(self):
        return self.by_text(u"授权管理")
    # 定位HDFS
    def hdfs_manger(self):
        return self.by_text("HDFS")
    """创建功能相关输入框按钮定位"""
    # 定位创建按钮
    def create_btn(self):
        return self.by_id("create")
    def policy_name(self):
        return self.by_id("policy_name")
    def resource_path(self):
        return self.by_id("resource_path")
    def desc(self):
        return self.by_id("description")
    def add_btn(self):
        # return self.by_class("layui-icon")
        return self.js("$('.layui-icon').click()")
    # 定位组、用户、权限，返回一个列表
    def selects(self):
        return self.by_all_css("input.select2-search__field")
    def proxy_grant(self):
        return self.by_id("id15").click()
    # 定位用户组权限中的删除按钮
    def btn_stop(self):
        return self.js("$('.btn.stop').click()")
    def tj_btn(self):
        return self.js("$('#tj_buttion').click()")
        
    def qx_btn(self):
        return self.js("$('#xq_buttion').click()")
        

    """编辑功能相关输入框按钮定位"""
    # 定位所有编辑按钮，返回一个列表，编辑界面其它输入框、按钮和创建功能中用到的定位相同
    def edit_btn(self):
        return self.by_all_id("edit")
    
    """删除功能相关输入框按钮定位"""
    # 定位策略列表删除按钮
    def del_btn(self):
        return self.by_all_css("#del-click-accredit")
    # 弹出框【确认】按钮
    def del_yes(self):
        return self.by_css('a.layui-layer-btn0')
    # 弹出框【取消】按钮
    def del_no(self):
        return self.by_css('a.layui-layer-btn1')
    """获取界面内容相关"""
    # 获取所有策略名
    def get_name(self):
        return self.by_all_css("tr td:nth-child(2)")
  
    """业务逻辑代码"""
    # 创建 policy
    def create_policy(self, name, path, description, group, user, privilege, proxy=None, sub = None):
        self.create_btn().click()
        self.policy_name().clear()
        self.policy_name().send_keys(name)
        self.resource_path().clear()
        self.resource_path().send_keys(path)
        self.desc().clear()
        self.desc().send_keys(description)
        time.sleep(1)
        self.add_btn()
        time.sleep(2)
        # all_list = self.driver.find_elements_by_css_selector('input.select2-search__field')
        all_list = self.selects()
        print(all_list,type(all_list))
        all_list[0].send_keys(group)
        all_list[0].send_keys(Keys.ENTER)
        all_list[1].send_keys(user)
        all_list[1].send_keys(Keys.ENTER)
        all_list[2].send_keys(privilege)
        all_list[2].send_keys(Keys.ENTER)
        # 条件满足，勾选代理
        if proxy == "click":
            self.proxy_grant().click()
        # y 提交
        if sub in ['Y', 'y']:
            self.tj_btn() 
        else:
            self.qx_btn()
        time.sleep(2)
        return self.get_name()[-1].text
    
    # 编辑 policy
    def edit_policy(self, name, path, description, group, user, privilege, proxy=None, sub = None):
        self.edit_btn()[-1].click()
        self.policy_name().clear()
        self.policy_name().send_keys(name)
        self.resource_path().clear()
        self.resource_path().send_keys(path)
        self.desc().clear()
        self.desc().send_keys(description)
        time.sleep(1)
        self.add_btn()
        time.sleep(2)
        all_list = self.selects()
        print(all_list,type(all_list))
        all_list[3].send_keys(group)
        all_list[3].send_keys(Keys.ENTER)
        all_list[4].send_keys(user)
        all_list[4].send_keys(Keys.ENTER)
        all_list[5].send_keys(privilege)
        all_list[5].send_keys(Keys.ENTER)

        if proxy == "click":
            self.proxy_grant().click()
        # y 提交
        if sub in ['Y', 'y']:
            self.tj_btn() 
        else:
            self.qx_btn()
        time.sleep(2)
        return self.get_name()[-1].text   
    # 删除 policy
    def del_policy(self):
        time.sleep(1)
        self.del_btn()[-1].click()
        self.del_yes().click()
        # else:
        #     self.del_no().click()
        

