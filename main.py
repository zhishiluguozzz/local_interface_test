import pymysql
import os
import json
from flask_cors import *
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
from flask import Flask,request
app = Flask(__name__)


c_hosts = "localhost"
c_user = "admin"
c_passwd = "123"
c_db = "test"

@app.route('/get1', methods=[ 'get' ])
def gettest():
    connect = pymysql.connect(host=c_hosts, user=c_user, passwd=c_passwd, database=c_db, charset='utf8')
    cur = connect.cursor()
    sql = "select * from student"
    cur.execute(sql)
    data = cur.fetchall()
    para = []
    for i in data:
        text = {'id': i[0], 'name': i[1], 'major': i[2], 'grade': i[3]}
        para.append(text)
    return json.dumps(para,ensure_ascii=False,indent=4)


@app.route('/post1', methods=['post'])
def nametest():
    input = request.json.get('input')
    data = posttest(input)
    return data

def posttest(input):
    connect = pymysql.connect(host=c_hosts, user=c_user, passwd=c_passwd, database=c_db, charset='utf8')
    cur = connect.cursor()
    sql = "select * from student where name='%s'" % input
    cur.execute(sql)
    data = cur.fetchall()
    para =[]
    for i in data:
        text = {'id': i[0], 'name': i[1], 'major': i[2], 'grade': i[3]}
        para.append(text)
    return json.dumps(para, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    app.run(host='0.0.0.0')