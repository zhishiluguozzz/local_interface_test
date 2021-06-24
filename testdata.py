import pymysql
def sqldata():
    dbtest = pymysql.connect(host="localhost",user="admin",passwd="123",database="test",charset="utf8")
    corsor = dbtest.cursor()
    corsor.execute("drop table student")
    corsor.execute("create table if not exists student(id int primary key,name varchar(60),major varchar(60),grade int)")
    insert_sql = "insert into student values(1,'张三','计算机',85),(2,'李四','物联网',47),(3,'王五','通信',68),(4,'赵六','微电子',95)"
    corsor.execute(insert_sql)