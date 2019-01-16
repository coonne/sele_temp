#weibo auto search
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("http://weibo.com/")
sleep(15)
driver.find_element_by_xpath("//input[@node-type='searchInput']").send_keys("test")
driver.find_element_by_xpath("//a[@node-type='searchSubmit']").click()