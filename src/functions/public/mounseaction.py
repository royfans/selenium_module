# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


brower = webdriver.Chrome()
brower.get("http://www.baidu.com")
#brower.maximize_window()
# 1、鼠标悬停，点击
move_mouse = brower.find_element_by_link_text("设置")
ActionChains(brower).move_to_element(move_mouse).perform()
brower.find_element_by_link_text("高级搜索").click()

# 2、鼠标双击操作
# 定位到要双击的元素
qqq = driver.find_element_by_xpath("xxx")
# 对定位到的元素执行鼠标双击操作
ActionChains(driver).double_click(qqq).perform()

# 3、鼠标元素拖放操作
#定位元素的原位置
element = driver.find_element_by_name("source")
#定位元素要移动到的目标位置
target =  driver.find_element_by_name("target")

#执行元素的移动操作
ActionChains(driver).drag_and_drop(element, target).perform()
'''
ActionChains 类提供的鼠标操作的常用方法

perform() 执行所有ActionChains中存储的行为
context_click()  右击
double_click()  双击
drag_and_drop()  拖动
move_to_element() 鼠标悬停
'''
