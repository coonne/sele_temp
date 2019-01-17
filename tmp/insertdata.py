#落库实验
import pymysql
from time import sleep

db = pymysql.connections.Connection(host='www.gytech.vip',user='gytech',password='wegmxn#e27bVR(',port=55944,database='gytech_main')

sleep(5)

cur = db.cursor()

sql_inster = """insert into wb_stat(wb_login,wb_sec,wb_desc) values ('coonnesuper@163.com','Zhang12347','testacc1')"""
try:
    cur.execute(sql_inster)
    db.commit()
except Exception as e:
    db.rollback()
finally:
    db.close()