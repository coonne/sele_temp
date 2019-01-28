from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
pro_option = Options()
pro_option.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=pro_option)
#driver = webdriver.Chrome() #调用chrome
driver.get("https://weibo.com/2803301701/HdU4sfqG3?type=comment") #进入主页
sleep(10)
print (driver.find_element_by_xpath("//span[@node-type='like_status']").text)  # 打印字符
#print (driver.find_element_by_xpath("//div[@node-type='focusLink']").text) # 打印字符
#driver.find_element_by_name("//")
