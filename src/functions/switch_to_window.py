# coding=utf-8

from selenium import webdriver
import time
driver = webdriver.Firefox()

driver.get("http://www.baidu.com/")

handle = driver.current_window_handle
print("handle:")
driver.find_element_by_id("kw").send_keys("python")
driver.find_element_by_id("su").click()
time.sleep(4)
driver.find_element_by_partial_link_text("基础教程 | 菜鸟教程").click()
time.sleep(3)
hadles = driver.window_handles

for newhandle in hadles:
    if newhandle != handle:
        print(newhandle)
        driver.switch_to.window(newhandle)
        driver.find_element_by_id("s").send_keys("python")
        time.sleep(4)
        driver.close()

driver.switch_to.window(hadles[0])


