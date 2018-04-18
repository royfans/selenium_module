# coding=utf-8

from .baseaction import Baseaction
import time

class GroupManagePage(Baseaction):

     # 定位认证管理
    def auth_manage(self):
        return self.by_text(u"认证管理")
    # 定位组管理
    def group_manage(self):
        return self.by_text(u"组管理")
    """创建组相关定位"""
    # 定位创建按钮
    def add_group(self):
        return self.by_id("addGroup-click")
    # 定位组名
    def group_name(self):
        return self.by_id("group_name")
    # 定位组描述
    def group_desc(self):
        return self.by_id("group_desc")
    # 定位管理员
    def group_manger(self):
        # 定位已 text 开头的用户
        self.by_css("ul>li>input.select2-search__field").send_keys("test")
        time.sleep(1)
        # 定位所有包含 text 的用户，返回一个用户列表
        return self.by_all_class("select2-results__option")
    # 定位立即提交按钮
    def submit(self):
        return self.by_id("create_group")
    # 定位重置按钮
    def layui_btn(self):
        return self.by_css("button.layui-btn.layui-btn-primary")
    # 定位管理组界面所有的用户，返回用户列表
    def all_group_names(self):
        return self.by_all_css("tr > td:nth-child(2) > a")

    """编辑组"""
    def edit_btn(self):
        return self.by_all_id("editGroup-click")
    """删除组"""
    # 删除按钮
    def del_btm(self):
        return self.by_all_css("#del-group")
    # 定位删除弹出框【确认删除】按钮
    def del_yes(self):
        return self.by_css("a.layui-layer-btn0")
    # 定位删除弹出框【取消】按钮
    def del_no(self):
        return self.by_css("a.layui-layer-btn1") 
    # 创建组
    def create_group(self, grp_name, grp_desc, manage_num):
        self.add_group().click()
        self.group_name().clear()
        self.group_name().send_keys(grp_name)
        self.group_desc().clear()
        self.group_desc().send_keys(grp_desc)
        time.sleep(2)
        # if int(manage_num) > len(res):
        #     print("用户数量不足")
        for num in range(manage_num):
            self.group_manger()[num].click()
        self.submit().click()
        time.sleep(1)
        return self.all_group_names()[-1].text
    
    # 编辑组
    def edit_group(self, grp_name, grp_desc):
        time.sleep(1)
        self.edit_btn()[-1].click()
        self.group_name().clear()        
        self.group_name().send_keys(grp_name)
        self.group_desc().clear()        
        self.group_desc().send_keys(grp_desc)
        self.submit().click()
        time.sleep(1)
        return self.all_group_names()[-1].text

    # 删除组
    def del_group(self):
        self.del_btm()[-1].click()
        self.del_yes().click()
        
        



