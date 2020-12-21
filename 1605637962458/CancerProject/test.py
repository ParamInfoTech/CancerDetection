import sqlite3
# commented part will be required in future while using SQLAlchemy
from flask import Flask, request, render_template
# from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
# db = SQLAlchemy(app)


@app.route("/",methods=["POST","GET"])

def senddata():
    f={}
    if request.method=="POST":
        result=request.form
        print("Gauranga")
        conn=sqlite3.connect("test.db")
        # conn.row_factory = sqlite3.Row
        c=conn.cursor()
        # just dropped table for debugging purpose
        # c.execute("drop table if exists dbtest")
        # conn.commit()
        # print(result["age"])
        if result["age"]!="":
            print (result["age"],'Nitai');
            c.execute('CREATE TABLE if not exists dbtest( p_id INT,name TEXT,age INT, date TEXT, d_name TEXT ,m_status INT,BF_History INT,First_Pregnancy_age INT,f_history INT, R_history INT,b_history INT,self_history INT,Medicine_history INT )')
            c.execute('INSERT INTO dbtest VALUES(%d,"%s",%d,"%s","%s",%d,%d,%d,%d,%d,%d,%d,%d)'%(int(result["id"]),result["p_name"],int(result["age"]),result["date"],result["d_name"],int(result["mstatus"]),int(result["BF_History"]), int(result["1Pregnancy_age"]),int(result["f_history"]),int(result["R_history"]), int(result["b_history"]),int(result["self_history"]),int(result["Medicine_history"])))
            conn.commit()

            print(result["p_name"])
            print(result["age"])
        # patientName=result["p_name"]
        c.execute('SELECT * FROM dbtest')
        f=c.fetchall()
        print("your data is:")
        for i in f:
            print(i)

        conn.close()
    #     class Patient():
    #         patient_id=db.Column(db.Integer,primary_key=True)
    #         patient_name= db.Column(db.String(30))
    #         age = db.Column(db.Integer)
    #         referred_by = db.Column(db.String(30))
    #         date = db.Column(db.String(30))
    #         martial_status = db.Column(db.Integer)
    #         BF_history = db.Column(db.Integer)
    #         First_Pregnancy_age = db.Column(db.Integer)
    #         f_history = db.Column(db.Integer)
    #         R_history = db.Column(db.Integer)
    #         b_history = db.Column(db.Integer)
    #         self_history = db.Column(db.Integer)
    #         Medicine_history = db.Column(db.Integer)
    #
    #         # def __init__(self,):

    return render_template("formh.html",data=f)

if(__name__=="__main__"):
    app.run(debug=True)

#
# conn=sqlite3.connect("test.db")
# c=conn.cursor()
# c.execute("drop table dbtest")
# conn.commit()
