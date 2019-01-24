import pymysql.cursors

db = pymysql.connections.Connection(host='www.gytech.vip',user='gytech',password='wegmxn#e27bVR(',port=55944,database='gytech_main')

try:
    with db.cursor() as cursor:
        sql1 = 'select * from wb_stat where wb_num >= 1 '
        count1 = cursor.execute(sql1)


        print(count1)

        count2 = cursor.fetchall()

        for i in count2:
            print(i)
        db.commit()
        #for i in result:
      #      print(i)
       # db.commit()
except:
    db.rollback()
finally:
    db.close()

