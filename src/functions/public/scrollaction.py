# coding=utf-8
# Program:
#         封装滚动条常用操作的一些公共方法
# Histroy:
# 2017/10/29 Royfans First release
from selenium import webdriver
import time
class Scrollaction(object):
    """

    """
    def __init__(self, driver):
        self.driver = driver
    # 滚动到最顶部
    def scroll_top(self):
        js = "window.scrollTo(0,0)"
        self.driver.execute_script(js)
    # 滚动到最底部
    def scroll_bottom(self):
        js = "window.scrollTo(0,document.body.scrollHeight)"
        self.driver.execute_script(js)
    # 聚焦元素
    def scroll_id(self,id):
        target = driver.find_element_by_id(id)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

if __name__ == "__main__":
    driver = webdriver.Chrome()
    sa = Scrollaction()
    driver.get("http://www.cnblogs.com/yoyoketang/p/6128655.html")
    time.sleep(3)
    sa.scroll_bottom()
    time.sleep(2)
    sa.scroll_top()
    time.sleep(2)
    driver.close()