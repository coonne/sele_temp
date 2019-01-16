#weibo auto login 模拟
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("http://weibo.com/")
sleep(15)
driver.find_element_by_xpath("//input[@node-type='username']").send_keys("coonne")
sleep(3)
driver.find_element_by_xpath("//input[@node-type='password']").send_keys("Zhang12347")

driver.find_element_by_xpath("//a[@node-type='submitBtn']").click()