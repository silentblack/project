import pymysql
db=pymysql.connect(host="localhost",port=3306,user="root",password="123456",database="students",charset="utf8")
cur=db.cursor()
name=input("Name:")
sql="select name,age,score from cls where name='%s';"%name
cur.execute(sql)
print(cur.fetchall())
cur.close()
db.close()