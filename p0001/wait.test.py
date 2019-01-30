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
            sql1 = 'select * from wb_temp where wb_num limit 1,11'
            dbops1 = cursor.execute(sql1)
            dbops2 = cursor.fetchall()
            for i in dbops2:
                wb_base(i[1], i[2])
                driver = webdriver.Chrome() #调用chrome
                driver.get("https://weibo.com/1694841822/He3oEroRe?from=page_1005051694841822_profile&wvr=6&mod=weibotime&type=comment#_loginLayer_1548740458687") #进入博主主页
                sleep(20)
                driver.find_element_by_xpath("//span[@node-type='like_status']").click()  # 点击第一条微博的LIKE按钮