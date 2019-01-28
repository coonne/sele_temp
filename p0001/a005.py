import pymysql.cursors
from time import sleep


db = pymysql.connections.Connection(host='www.gytech.vip', user='gytech', password='wegmxn#e27bVR(', port=55944, database='gytech_main')

def lg_ps(acc, pwd):
    print("%s , %s " %(acc, pwd))
    pass

try:
    with db.cursor() as cursor:
        sql1 = 'select * from wb_stat where wb_num >= 1 '
        Opt1 = cursor.execute(sql1)
        Opt2 = cursor.fetchall()
        for i in Opt2:
            lg_ps(i[1], i[2])
            sleep(90)
        db.commit()
except:
    db.rollback()
finally:
    db.close()

