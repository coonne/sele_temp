#weibo auto follow
from selenium import webdriver
from time import sleep


driver = webdriver.Chrome()
driver.get("https://weibo.com/u/1402977920")
sleep (10)
driver.find_element_by_xpath("//div[@node-type='focusLink']").click()
sleep(5)
driver.find_element_by_xpath("//input[@node-type='username']").send_keys("coonne")
sleep(5)
driver.find_element_by_xpath("//input[@node-type='password']").send_keys("Zhang12347")
sleep(2)
driver.find_element_by_xpath("//a[@node-type='submitBtn']").click()
sleep(10)
driver.find_element_by_xpath("//div[@node-type='focusLink']").click()