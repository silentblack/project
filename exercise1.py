import pymysql
db=pymysql.connect(host="localhost",port=3306,user="root",password="123456",charset="utf8")
cur=db.cursor()
f=open("dict.txt","r")
sql_1="create database dict;"
sql_2="use dict; "
sql_3="create table word(id int primary key auto_increment,word varchar(30),mean text, index(word));"
# cur.execute(sql_1)
# cur.execute(sql_2)
# cur.execute(sql_3)
list_word=[]
for i in f:
    item=i.split(" ",1)
    print(item)
    list_word.append(item)
sql="insert into table words(word,mean) values(%s,%s);"
try:
    cur.executemany(sql,list_word)
    db.commit()
except Exception as e:
    print(e)
    db.rollback()
cur.close()
db.close()
