from pickle import NONE
import pymysql
from flask import Flask, render_template, request, jsonify, url_for, redirect,session
from flask_session import Session

from flask_mysqldb import MySQL
# import pyyaml 

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

app.config['MYSQL_HOST']='bjb8svdmd7sj7ta1dbng-mysql.services.clever-cloud.com'
app.config['MYSQL_USER']='u3aeixuubn1povrx'
app.config['MYSQL_PASSWORD']='XKlynAYY3Zu46pfvgOQt'
app.config['MYSQL_DB']='bjb8svdmd7sj7ta1dbng'

mysql=MySQL(app)


@app.route('/')
def index():
    return render_template('index.html')
nz=""
ls=""

@app.route('/login_client.html', methods=['GET','POST'])
def login_client():
    if request.method=='POST':
        userDetails=request.form
        name=userDetails["name"]
        mobileno=userDetails["mobile no."]
        lisence=userDetails["lisence"]
        password=userDetails["password"]
        
        cur=mysql.connection.cursor()
        
        s="select mobile,name,password,registration_no from CLIENT where mobile="+'"'+mobileno+'" '+" and name="+'"'+name+'"'+"and password="+'"'+password+'"'+";"
        # print(s)
        cur.execute(s)
        row=cur.fetchone()
        cur.close()
        q="select * from cars where registartion_no="+'"'+lisence+'" '+" and name="+'"'+name+'"'+";"
        cur=mysql.connection.cursor()
        cur.execute(q)
        rz=cur.fetchone()
        # print("YE",rz)
        cur.close()
        if rz !=None and row!=None:
            session["nme"]=name
            session["lsence"]=lisence
            print(rz)
            return render_template('loged_client.html',data=rz,data2=row)
        else:
            return '!!!WRONG CREDENTIALS!!!'
        # mysql.connection.commit()
    return render_template('login_client.html')

@app.route('/login_dealer.html', methods=['GET','POST'])
def login_dealer():
    if request.method=='POST':
        userDetails=request.form
        name=userDetails["name"]
        lisence=userDetails["lisence"]
        password=userDetails["password"]
        
        cur=mysql.connection.cursor()
        s="select name,license_no,password from dealership where name="+'"'+name+'" '+" and license_no="+'"'+lisence+'"'+" and password="+'"'+password+'"'+";"
        # print(s)
        cur.execute(s)
        row=cur.fetchone()
        cur.close()
        if row !=None:
            # return name,mobileno,lisence,password
            return render_template('loged_delear.html',a='Card info',name=name,Lisence=lisence)

        # print(dz)
        else:
            return '!!!WRONG CREDENTIALS!!!'
    return render_template('login_dealer.html')

@app.route('/sign_in_client.html', methods=['GET','POST'])
def sign_in_client():
    if request.method=='POST':
        userDetails=request.form
        name=userDetails["name"]
        mobileno=userDetails["mobile no."]
        lisence=userDetails["lisence"]
        password=userDetails["password"]
        car_company=userDetails["car_company"]
        car_model=userDetails["car_model"]
        city=userDetails["city"]
        insurance_company=userDetails["insurance_company"]
        insurance_plan=userDetails["insurance_plan"]
        insurance_id=userDetails["insurance_id"]
        insurance_price=userDetails["insurance_price"]
        insurance_date=userDetails["insurance_date"]
        maintenance_plan=userDetails["maintenance_plan"]
        maintenance_price=userDetails["maintenance_price"]
        maintenance_company=userDetails["maintenance_company"]
        maintenance_date=userDetails["maintenance_date"]
        maintenance_due=userDetails["maintenance_due"]
        maintenance_id=userDetails["maintenance_id"]
        puc=userDetails["puc"]
        license=userDetails["license"]
        chasis_no=userDetails["chasis_no"]
        rc_no=userDetails["rc_no"]
        license_expiry=userDetails["license_expiry"]
        puc_expiry=userDetails["puc_expiry"]
        rc_expiry=userDetails["rc_expiry"]

        cur=mysql.connection.cursor()
        cur.execute("INSERT INTO CLIENT (mobile,name,password,registration_no) VALUES(%s,%s,%s,%s);",(mobileno,name,password,lisence))
        mysql.connection.commit()
        cur=mysql.connection.cursor()
        cur.execute("INSERT INTO cars (name,registartion_no,car_company,model,city,insurance_company,insurance_plan,insurance_id,insurance_price,insurance_date,maintenance_plan,maintenance_price,maintenance_company,maintenance_date,maintenance_due,maintenance_id,puc,license,chasis_no,rc_no,license_expiry,puc_expiry,rc_expiry) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);",(name,lisence,car_company,car_model,city,insurance_company,insurance_plan,insurance_id,insurance_price,insurance_date,maintenance_plan,maintenance_price,maintenance_company,maintenance_date,maintenance_due,maintenance_id,puc,license,chasis_no,rc_no,license_expiry,puc_expiry,rc_expiry));
        mysql.connection.commit()
        cur.close()
        return login_client()
    return render_template('sign_in_client.html')

@app.route('/sign_in_dealer.html', methods=['GET','POST'])
def sign_in_dealer():
    if request.method=='POST':
        userDetails=request.form
        name=userDetails["name"]
        mobileno=userDetails["mobile no."]
        license=userDetails["lisence"]
        city=userDetails["city"]
        password=userDetails["password"]
        cur=mysql.connection.cursor()
        cur.execute("INSERT INTO dealership (mobile,name,city,license_no,password) VALUES(%s,%s,%s,%s,%s);",(mobileno,name,city,license,password))
        mysql.connection.commit()
        cur.close()
        return login_dealer()
        # return 'success'
    return render_template('sign_in_dealer.html')

@app.route('/insurance.html',methods=['GET','POST'])
def insurance():
    # if request.method=='POST':
    cur=mysql.connection.cursor()
    nq=session.get("nme",None)
    lq=session.get("lsence", None)
    
    s="select * from car where name="+'"'+nq+'" '+" and registration_no="+'"'+lq+'"'+";"
    # print(s)
    cur.execute(s)
    rz=cur.fetchone()
    cur.close()
    if(rz==None):
        return "NO INSURANCE AVAILABLE"
    # print(rz,rz[-1])
    r="select * from insurance where city="+'"'+rz[-1]+'"'+';'
    curr=mysql.connection.cursor()
    curr.execute(r)
    row=curr.fetchall()
    print(row)
    curr.close()
    if(row!=NONE):
        return render_template('insurance.html',data=row)
    else:
        return "NO INSURANCE AVAILABLE"
    # return render_template('insurance.html')

@app.route('/servicing.html')
def servicing():
    cur=mysql.connection.cursor()
    nq=session.get("nme",None)
    lq=session.get("lsence", None)
    
    s="select * from car where name="+'"'+nq+'" '+" and registration_no="+'"'+lq+'"'+";"
    # print(s)
    cur.execute(s)
    rz=cur.fetchone()
    cur.close()
    if(rz==None):
        return "NO INSURANCE AVAILABLE"
    print(rz,rz[-1])
    r="select * from servicing where city="+'"'+rz[-1]+'"'+"and car_company="+'"'+rz[2]+'"' +';'
    curr=mysql.connection.cursor()
    curr.execute(r)
    row=curr.fetchall()
    print(row)
    curr.close()
    if(row!=NONE):
        return render_template('servicing.html',data=row)
    else:
        return "NO SERVICING AVAILABLE"
    

@app.route('/insurance_add.html', methods=['GET','POST'])
def insurance_add():
    if request.method=='POST':
        userDetails=request.form
        name=userDetails["name"]
        city=userDetails["city"]
        car_company=userDetails["car_company"]
        company=userDetails["company"]
        plan=userDetails["plan"]
        price=userDetails["price"]
        link=userDetails["link"]
        cur=mysql.connection.cursor()
        cur.execute("insert into insurance(car_company,delearship,company,plan,price,city,link) values(%s,%s,%s,%s,%s,%s,%s);",(car_company,name,company,plan,price,city,link))
        mysql.connection.commit()
        cur.close()
        return render_template('done.html')
    return render_template('insurance_add.html')



@app.route('/servicing_add.html', methods=['GET','POST'])
def servicing_add():
    if request.method=='POST':
        userDetails=request.form
        car_company=userDetails["car_company"]
        cname=userDetails["cname"]
        plan=userDetails["plan"]
        price=userDetails["price"]
        city=userDetails["city"]
        mobileno=userDetails["mobile"]
        print(cname,plan,car_company,price)
        cur=mysql.connection.cursor()
        cur.execute("insert into servicing(car_company,delearship,plan,price,city,mobile_no) values(%s,%s,%s,%s,%s,%s);",(car_company,cname,plan,price,city,mobileno))
        mysql.connection.commit()
        cur.close()
        return render_template('done.html')
    return render_template('servicing_add.html')



if __name__=='__main__':
    app.run(debug=True)
