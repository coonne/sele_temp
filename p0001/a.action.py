from selenium import webdriver
from time import sleep
import pymysql.cursors
from selenium.webdriver.chrome.options import Options

db = pymysql.connections.Connection(host='www.gytech.vip', user='gytech', password='wegmxn#e27bVR(', port=55944,database='gytech_main')
def wb_base(Wb_Acc, Wb_lgn):

    print("%s, %s" %(Wb_Acc, Wb_lgn))

    pass

try:
         with db.cursor() as cursor:
            sql1 = 'select * from wb_stat where wb_num limit 1,11'
            dbops1 = cursor.execute(sql1)
            dbops2 = cursor.fetchall()
            for i in dbops2:
                wb_base(i[1], i[2])
                driver = webdriver.Chrome() #调用chrome
                driver.get("https://weibo.com/1694841822/He3oEroRe?from=page_1005051694841822_profile&wvr=6&mod=weibotime&type=comment#_loginLayer_1548740458687") #进入博主主页
                sleep(20)
                driver.find_element_by_xpath("//span[@node-type='like_status']").click()  # 点击第一条微博的LIKE按钮
                #print (driver.find_elements_by_xpath("//span[@node-type='like_status']"))
                #driver.find_element_by_xpath("//div[@node-type='focusLink']").click()  # 点击关注
                sleep(5)
                driver.find_element_by_xpath("//input[@node-type='username']").send_keys(str(i[1]))  # 弹出登录窗口输入账号
                sleep(5)
                driver.find_element_by_xpath("//input[@node-type='password']").send_keys(str(i[2]))  # 弹出登录窗口输入密码
                sleep(4)
                driver.find_element_by_xpath("//a[@node-type='submitBtn']").click()  # 弹出登录窗口点击登录按钮




                #sleep(10)
                #driver.find_element_by_xpath("//div[@node-type='focusLink']").click()  # 点击博主主页上的关注
                sleep(5)
                driver.find_element_by_xpath("//span[@node-type='like_status']").click()  # 点击第一条微博的LIKE按钮
                #driver.find_element("node-type", "like_status").click()
                sleep(5)
                #driver.find_element_by_xpath("//span[@node-type='forward_btn_text']").click()#第一条微博的转发按钮
                #sleep(5)
                #driver.find_element_by_xpath("//textarea[@node-type='textEl']").send_keys("可以可以")#弹出转发窗口输入内容
                #sleep(5)
                #driver.find_element_by_xpath("//input[@node-type='originInput']").click()#弹出转发窗口，勾选同时评论
                #sleep(3)
                #driver.find_element_by_xpath("//a[@node-type='submit']").click()#弹出转发窗口中转发按钮

                #sleep(90)
                driver.close()

            db.commit()


except:
             db.rollback()
finally:
              db.close()


#def wb_action(Once_Action):
    #driver = webdriver.Chrome()
    ## 运行
    #driver.get("https://weibo.com/531456966?topnav=1&wvr=6&topsug=1&is_hot=1")  # 进入博主主页
#
    #sleep(10)
    #driver.find_element_by_xpath("//div[@node-type='focusLink']").click()  # 点击关注
    #sleep(5)
    #driver.find_element_by_xpath("//input[@node-type='username']").send_keys('1')  # 弹出登录窗口输入账号
    #sleep(5)
    #driver.find_element_by_xpath("//input[@node-type='password']").send_keys('2')  # 弹出登录窗口输入密码
    #sleep(4)
    #driver.find_element_by_xpath("//a[@node-type='submitBtn']").click()  # 弹出登录窗口点击登录按钮
    #sleep(10)
    #driver.find_element_by_xpath("//div[@node-type='focusLink']").click()  # 点击博主主页上的关注
    #sleep(5)
    #driver.find_element_by_xpath("//span[@node-type='like_status']").click()  # 点击第一条微博的LIKE按钮
    #sleep(10)
    #driver.find_element_by_xpath("//span[@node-type='forward_btn_text']").click()#第一条微博的转发按钮
    #sleep(5)
    #driver.find_element_by_xpath("//textarea[@node-type='textEl']").send_keys("可以可以")#弹出转发窗口输入内容
    #sleep(5)
    #driver.find_element_by_xpath("//input[@node-type='originInput']").click()#弹出转发窗口，勾选同时评论
    #sleep(3)
    ## driver.find_element_by_xpath("//a[@node-type='submit']").click()#弹出转发窗口中转发按钮


