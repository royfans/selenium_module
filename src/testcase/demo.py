# condig=utf-8
import os
from src.common.initdriver import read_config
import time
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
url = "http://10.2.46.93:6080/login.jsp"
driver.get(url)
time.sleep(2)
driver.find_element_by_id("username").send_keys("admin")
driver.find_element_by_id("password").send_keys("admin")
driver.find_element_by_id("signIn").click()
time.sleep(2)
# driver.find_element_by_link_text(u"认证管理").click()
# driver.find_element_by_link_text(u"用户管理").click()
# driver.find_element_by_link_text(u"认证管理").click()
# driver.find_element_by_css_selector("tr:last>td.name")

#all_users > tbody > tr:nth-child(15) > td.name
driver.find_element