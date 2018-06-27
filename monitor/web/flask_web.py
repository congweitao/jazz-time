#!/usr/bin/env python

import MySQLdb as mysql
import json
from flask import Flask, request, render_template

app = Flask(__name__)
db = mysql.connect(user="root", passwd="123456", \
        db="congwt", charset="utf8")
db.autocommit(True)
c = db.cursor()

@app.route("/")
def index():
    return render_template("monitor.html")

tmp_time = 0

@app.route("/data")
def getdata():
    '''第一次查询全量数据，后面只查询增量数据'''
    global  tmp_time
    if tmp_time > 0 :
        sql = "select time,mem_free from stat where time >%s" %(tmp_time)
    else:
        sql = "select time,mem_free from stat"
    cur.execute(sql)
    datas = []
    for i in cur.fetchall():
        datas.append([i[0], i[1]])

    if len(datas) > 0 :
        tmp_time = datas[-1][0]

    return json.dumps(datas)


if __name__ == "__main__":
    app.run(host='10.0.50.106',port=8888,debug=True) 
