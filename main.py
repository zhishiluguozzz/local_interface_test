import pymysql
import os
import json
from flask_cors import *
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
from flask import Flask,request
app = Flask(__name__)

@app.route('/get1',methods=[ 'get'])
def gettest():
    conn = pymysql.connect(host="localhost",user="admin",passwd="123",database="test",charset="utf8")
    cur = conn.cursor()
    sql = "select * from student"
    cur.execute(sql)
    data = cur.fetchall()
    para = []
    for i in data:
        text = {'id':i[0],'name':i[1],'major':i[2],'grade':i[3]}
        para.append(text)
    return json.dumps(para,ensure_ascii=False,indent=4)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8081)