from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from time import sleep
import pymysql.cursors
#from selenium.webdriver.chrome.options import Options

db = pymysql.connections.Connection(host='www.gytech.vip', user='gytech', password='wegmxn#e27bVR(', port=55944, database='gytech_main')

def wb_base(Wb_Acc, Wb_lgn):

    print("%s, %s" %(Wb_Acc, Wb_lgn))

    pass

try:
         with db.cursor() as cursor:
            sql1 = 'select * from wb_stat where wb_num >=1'
            dbops1 = cursor.execute(sql1)
            dbops2 = cursor.fetchall()
            #Wb_url = input(str("pls input url:"))
            #print(Wb_url)
            for i in dbops2:
                wb_base(i[1], i[2])
                while True:
                    driver = webdriver.Chrome() #调用chrome
                    #driver.get("%s" %(Wb_url))
                    driver.get("") #进入博主主页
                    sleep(20)
                    driver.find_element_by_xpath("//span[@node-type='like_status']").click()  # 点击第一条微博的LIKE按钮
                    sleep(3)
                    driver.find_element_by_xpath("//input[@node-type='username']").send_keys(str(i[1]))  # 弹出登录窗口输入账号
                    sleep(5)
                    driver.find_element_by_xpath("//input[@node-type='password']").send_keys(str(i[2]))  # 弹出登录窗口输入密码
                    sleep(5)
                    driver.find_element_by_xpath("//a[@node-type='submitBtn']").click()  # 弹出登录窗口点击登录按钮
                    sleep(6)

                    try:
                      driver.find_element_by_xpath("//span[@node-type='like_status']").click()  # 点击第一条微博的LIKE按钮


                    except WebDriverException as e:
                        pass

                    break
                driver.close()


except Exception as e:
    print(e.with_traceback())

    db.rollback()
finally:
    db.close()


