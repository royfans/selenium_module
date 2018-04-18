# coding=utf-8

# Program:
#         封装元素常用操作的一些公共方法
# Histroy:
# 2017/10/28 Royfans First release
from selenium import webdriver
class Baseaction(object):

    def __init__(self, driver):
        self.driver = driver
        # self.driver = webdriver.Firefox()

    def by_id(self, the_id):
        return self.driver.find_element_by_id(the_id)

    def by_all_id(self, the_all_id):
        return self.driver.find_elements_by_id(the_all_id)

    def by_name(self, the_name):
        return self.driver.find_element_by_name(the_name)

    def by_class(self, the_class):
        return self.driver.find_element_by_class_name(the_class)

    def by_all_class(self, the_all_class):
        return self.driver.find_elements_by_class_name(the_all_class)

    def by_xpath(self, by_xpath):
        return self.driver.find_element_by_xpath(by_xpath)

    def by_css(self, by_css):
        return self.driver.find_element_by_css_selector(by_css)

    def by_all_css(self,by_all_css):
        return self.driver.find_elements_by_css_selector(by_all_css)
    # 通过界面上按钮的部分文本进行定位
    def by_text(self, by_text):
        return self.driver.find_element_by_link_text(by_text)
    # 通过界面上按钮的部分文本进行定位
    def by_partial_text(self, by_partial_text):
        return self.driver.find_element_by_partial_link_text(by_partial_text)
    # 执行js 语句
    def js(self, js_text):
        return self.driver.execute_script(js_text)

    def current_url(self):
        return self.driver.current_url

if __name__ == "__main__":
    driver = webdriver.Chrome()
    ba = Baseaction()
    driver.get("http://www.baidu.com")
    ba.by_id('kw').send_keys("python")
    driver.close()



