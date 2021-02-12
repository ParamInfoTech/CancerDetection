import sqlite3
from flask import Flask, request, render_template
import mysql.connector

app = Flask(__name__)

conn= mysql.connector.connect(host="localhost",user="root",password="") 
c=conn.cursor()
c.execute('create database if not exists test')
conn.close()

conn= mysql.connector.connect(host="localhost",user="root",password="",database="test") 
c=conn.cursor()


@app.route("/",methods=["POST","GET"])
def senddata():
    f = {}
    if request.method == "POST":
        result = request.form
        print("Gauranga")
        '''
        conn = sqlite3.connect("test.db")
        c = conn.cursor()
        '''
        if result["age"] != "":
            print(result["age"], 'Nitai');
            c.execute('CREATE TABLE if not exists dbtest( p_id INT,name TEXT,age INT, date TEXT,'
                      'd_name TEXT ,m_status INT,BF_History INT,First_Pregnancy_age INT,'
                      'f_history INT, R_history INT,b_history INT,self_history INT,Medicine_history INT )')
            c.execute('INSERT INTO dbtest VALUES(%d,"%s",%d,"%s","%s",%d,%d,%d,%d,%d,%d,%d,%d)' % (int(result["id"]), result["p_name"], int(result["age"]), result["date"], result["d_name"],int(result["mstatus"]), int(result["BF_History"]), int(result["1Pregnancy_age"]), int(result["f_history"]),int(result["R_history"]), int(result["b_history"]), int(result["self_history"]),int(result["Medicine_history"])))
            conn.commit()

        c.execute('SELECT * FROM dbtest')
        f = c.fetchall()
        print("your data is:")
        for i in f:
            print(i)

        conn.close()
    return render_template("formh.html", data=f)


if __name__=="__main__":
    app.run(debug=True)
