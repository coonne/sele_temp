#读数据库，遍历数据并打印
import pymysql

db = pymysql.connections.Connection(host='www.gytech.vip',user='gytech',password='wegmxn#e27bVR(',port=55944,database='gytech_main')

cur = db.cursor()
sql = "select * from wb_stat"

try:
        cur.execute(sql)
        results = cur.fetchall()
        print("wb_num","wb_login","wb_sec","wb_desc")

        for row in results:
            wb_num = row[0]
            wb_login = row[1]
            wb_sec = row[2]
            wb_desc = row[3]
            print(wb_num,wb_login,wb_sec,wb_desc)

except Exception as e:
        raise e
finally:
        db.close()