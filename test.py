from flask import Flask, request, render_template
import mysql.connector
import os
import cv2 as cv
IMAGE_FOLDER = os.path.join('static', 'images')

app = Flask(__name__)
app.config['IMAGE_FOLDER'] = IMAGE_FOLDER

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
        conn = getConnection()
        c = conn.cursor()
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


def getConnection():
    conn = mysql.connector.connect(
        host="katkarvijayd.mysql.pythonanywhere-services.com",
        user="katkarvijayd",
        password="poonam@87",
        database="patients"
    )
    return conn

def getImage(id, image_name):
    conn = getConnection()
    cursor = conn.cursor()
    sql_fetch_blob_query = """SELECT * from imagedb where p_id = %s and iname = %s"""

    cursor.execute(sql_fetch_blob_query, (id, image_name))
    record = cursor.fetchall()
    image_name = ""
    for row in record:
        print("Id = ", row[0], )
        print("Name = ", row[1])
        image = row[2]
        image_name = app.config['IMAGE_FOLDER'] + "/" + str(row[0]) + "_" + row[1] + ".jpg"
        print("image path : ", image_name)
        print("Storing employee image and bio-data on disk \n")
        with open(image_name, 'wb') as file:
            file.write(image)
    conn.close()
    return image_name

@app.route("/imageOps",methods=["POST","GET"])
def imageOps():
    return render_template("ImageOps.html")


@app.route("/edgeDetection",methods=["POST","GET"])
def edgeDetection():
    if request.method == "POST":
        return render_template("EdgeDetection.html")
    else:
        original_image_path = getImage(2, "img4")
        img = cv.imread(original_image_path)

        laplacian_result = cv.Laplacian(img, cv.CV_64F)
        laplacian_image_path= app.config['IMAGE_FOLDER'] + "/" + 'laplacian_'+ original_image_path.split("/")[-1]
        cv.imwrite(laplacian_image_path, laplacian_result)

        return render_template("EdgeDetection.html", original_image=original_image_path, laplacian= laplacian_image_path)


if __name__=="__main__":
    app.run(debug=True)
