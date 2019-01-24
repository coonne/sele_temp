#auto zhuanfa
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options



pro_option = Options()
pro_option.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=pro_option)



driver = webdriver.Chrome()
#运行
driver.get("https://weibo.com/531456966?topnav=1&wvr=6&topsug=1&is_hot=1")#进入博主主页

sleep (10)
driver.find_element_by_xpath("//div[@node-type='focusLink']").click()#点击关注
sleep(5)
driver.find_element_by_xpath("//input[@node-type='username']").send_keys("435006847@qq.com")#弹出登录窗口输入账号
sleep(5)
driver.find_element_by_xpath("//input[@node-type='password']").send_keys("AA1234567890")#弹出登录窗口输入密码
sleep(4)
driver.find_element_by_xpath("//a[@node-type='submitBtn']").click()#弹出登录窗口点击登录按钮
sleep(10)
driver.find_element_by_xpath("//div[@node-type='focusLink']").click()#点击博主主页上的关注
sleep(5)
driver.find_element_by_xpath("//span[@node-type='like_status']").click()#点击第一条微博的LIKE按钮
sleep(10)
#driver.find_element_by_xpath("//span[@node-type='forward_btn_text']").click()#第一条微博的转发按钮
sleep(5)
#driver.find_element_by_xpath("//textarea[@node-type='textEl']").send_keys("可以可以")#弹出转发窗口输入内容
sleep(5)
#driver.find_element_by_xpath("//input[@node-type='originInput']").click()#弹出转发窗口，勾选同时评论
sleep(3)
#driver.find_element_by_xpath("//a[@node-type='submit']").click()#弹出转发窗口中转发按钮


#打印
print (driver.title)