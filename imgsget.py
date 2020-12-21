import sqlite3
import cv2
from flask import Flask, request, render_template
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

app=Flask(__name__)

#currently form has only 1 input file img1

@app.route("/",methods=["POST","GET"])

def sendidata():
    if request.method=="POST":
        arr=['img1','img2','img3','img4','img5','img6'] 
        conn=sqlite3.connect("test.db")
        c=conn.cursor()
        #c.execute("drop table imagedb")
        
        def convertToBinaryData(filename):
            #Convert digital data to binary format
            with open(filename, 'rb') as file:
                blobData = file.read()
            return blobData
        
        def cptopc(blb):    
            with open("i1.jpg", "wb") as image:
                image.write(blb)
                image.close()
                
        pid=request.form['id']
        c.execute('CREATE TABLE if not exists imagedb(p_id INT,iname varchar(7),im BLOB)')          
        
        for i in arr:
            result=request.files[i]
            with open("i1.jpg", "wb") as image:
                image.write(result.read())
                image.close()
            f=convertToBinaryData("i1.jpg")
            c.execute('INSERT INTO imagedb(p_id,iname,im) VALUES (?,?,?)', (int(pid),i,f) )
        
        c.execute('SELECT count(*) from imagedb')
        i=c.fetchall()
        count=i[0][0]
        #following code is for displaying current  patient's uploaded images
        #not necessary other then debuging
        #start display
        try:
            c.execute('SELECT * FROM imagedb where p_id= %d'%(int(pid) ) )
            
            f=c.fetchall()
            l=len(f)
            for i in range(l):
                cptopc(f[i][2])
                plt.subplot(l//3,3,i+1).set_title("id"+str(f[i][0])+" "+str(f[i][1]))
                img = mpimg.imread("i1.jpg")
                plt.imshow(img)
            plt.show()
        except:
            print(" some other err occured")
        #end display
        c.execute('SELECT * FROM imagedb')
        f=c.fetchall()
        for i in f:
            print(i[0],i[1])
        
        conn.commit()
        c.close()
        conn.close()        
        print("Success")
        
    return render_template("iget.html")
        
        
if(__name__=="__main__"):
    app.run(debug=True)