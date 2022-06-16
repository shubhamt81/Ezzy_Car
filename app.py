import pymysql
from flask import Flask, render_template, request
from flask_mysqldb import MySQL
# import pyyaml 

app = Flask(__name__)


#configure db
# db=pyyaml.load(open('db.yaml'))
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='shubham@24'
app.config['MYSQL_DB']='ezzycar'


mysql=MySQL(app)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method=='POST':
        userDetails=request.form
        name=userDetails["name"]
        mobileno=userDetails["mobile no."]
        lisence=userDetails['lisence']
        password=userDetails['password']
        cur=mysql.connection.cursor()
        cur.execute("INSERT INTO CLIENT (mobile,name,password,registration_no) VALUES(%s,%s,%s,%s)",(mobileno,name,password,lisence))
        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template('index.html')

@app.route('/users')
def users():
    cur=mysql.connection.cursor()
    resultValue=cur.execute("SELECT * FROM CLIENT")
    if resultValue>0:
        userDetails=cur.fetchall()
        return render_template('users.html',userDetails=userDetails)

if __name__=='__main__':
    app.run(debug=True)

# def TupList(tup, lis):c
#     #print(tup)
#     for i in tup: 
#         #print(i)
#         lis.append(i)
#     return lis
# def hello_world():
#         result = request.form.to_dict()
#         print('Form data', result)
#         #print(result['Name'])
#         select = 0

#         host = 'localhost'
#         user = 'root'
#         password = 'shubham@24'
#         db = 'ezzycar'

# @app.route('/')
# def student():
#    return render_template('login.html')

# @app.route('/result',methods = ['POST', 'GET'])
# def hello_world():
#     if request.method == 'POST':
#         result = request.form.to_dict()
#         print('Form data', result)
#         #print(result['Name'])
#         select = 0

#         host = 'localhost'
#         user = 'root'
#         password = 'shubham@24'
#         db = 'Ezzycar'

#         final = []

#         try:
#             con = pymysql.connect(host=host, user=user, password=password, db=db, use_unicode=True, charset='utf8')
#             print('+=========================+')
#             print('|  CONNECTED TO DATABASE  |')
#             print('+=========================+')
#         except Exception as e:
#             print("error")
#         cur = con.cursor()
#         cur.execute("SELECT * FROM carspecification ")
#         data = cur.fetchall()
#         #print(data)
#         print(data[0][0])
#         print("debug")
#         for i in data:
#             print(i)

#         if(int(result['Name']) == int(data[0][0]) and result['Password'] == data[0][1]):
#             final = TupList(data[select], final)

#             cur.execute("SELECT * FROM carcare ")
#             data = cur.fetchall()
#             final = TupList(data[select], final)

#             cur.execute("SELECT * FROM cardocuments ")
#             data = cur.fetchall()
#             final = TupList(data[select], final)

#             cur.execute("SELECT * FROM carmaintenance ")
#             data = cur.fetchall()
#             final = TupList(data[select], final)

#             data = tuple(final)
#             di = {'info': data}
#             print(data)
#             print(di)
#             #print(data[select])#check username here and select appropriate index

#             return render_template('index.html',data = di)

#         else:
#             return render_template('err.html')

#         if (int(result['Name']) == int(data[1][0]) and result['Password'] == data[1][1]):
#             select=1
#             final = TupList(data[select], final)

#             cur.execute("SELECT * FROM carcare ")
#             data = cur.fetchall()
#             final = TupList(data[select], final)

#             cur.execute("SELECT * FROM cardocuments ")
#             data = cur.fetchall()
#             final = TupList(data[select], final)

#             cur.execute("SELECT * FROM carmaintenance ")
#             data = cur.fetchall()
#             final = TupList(data[select], final)

#             data = tuple(final)
#             di = {'info': data}
#             print(data)
#             print(di)
#             # print(data[select])#check username here and select appropriate index

#             return render_template('index.html', data=di)

#         else:
#             return render_template('err.html')
# if __name__ == '__main__':
#    app.run()
