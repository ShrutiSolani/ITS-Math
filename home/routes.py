from flask import Blueprint, render_template, request, flash, redirect, url_for, session, Flask, current_app
import json, os, random


import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="ITS"
)

home_bp = Blueprint('home_bp', __name__, template_folder = 'templates', static_folder='static')


@home_bp.route('/')
def index():
    return render_template('index.html')

@home_bp.route("/login")
def login():
    dict = {"message": "Login Page"}
    current_app.logger.info(json.dumps(dict))
    return render_template('login.html')

@home_bp.route("/login",methods=['POST'])
def logins():

    mycursor=mydb.cursor()
    if request.method=='POST':
        email=request.form['email']
        password=request.form['password']
        mycursor.execute("select * from Student where email='" + email + "' and password='" + password + "'")
        r = mycursor.fetchall()
        count = mycursor.rowcount
        mydb.commit()
        mycursor.close()
        if (count == 1):
            session['userid'] = r[0][0]
            dict = {"userid": session['userid'], "message": "Logged In"}
            current_app.logger.info(json.dumps(dict))
            return redirect('home')
        else:
            return redirect('logins')




@home_bp.route("/signup")
def signup():
    dict = {"message": "Signup Page"}
    current_app.logger.info(json.dumps(dict))
    return render_template('signup.html')

@home_bp.route("/signup",methods=['POST'])
def signups():

    if request.method=="POST":
        fname = request.form['fname']
        lname = request.form['lname']
        email = request.form['email']
        password = request.form['password']
        cpassword = request.form['cpassword']
        dob = request.form['dob']
        grade=request.form['grade']
        mycursor=mydb.cursor()
        mycursor.execute("Insert into Student(first_name,last_name,email,password,dob,grade)values(%s,%s,%s,%s,%s,%s)",(fname,lname,email,password,dob,grade))
        mydb.commit()
        mycursor.close()
        return redirect('login')
    else:
        return redirect('signup')

@home_bp.route("/home")
def home():
    mycursor=mydb.cursor()
    if 'userid' in session:
        mycursor.execute("select * from Student where id="+str(session['userid']))
        r = mycursor.fetchall()
        dict = {"userid": session['userid'], "message": "Home Page"}
        current_app.logger.info(json.dumps(dict))
        return render_template('home.html',name={'name':r[0][1]})
    else:
        return redirect('login')

@home_bp.route('/score', methods=['POST'])
def score():
    if request.method == 'POST':
        if 'userid' in session:
            userid=session['userid']
        count = 0

        tup = request.get_json('data')
        myList = list(tup.values())
        total = int(tup['undefined']) + int(tup['1']) + int(tup['2']) + int(tup['3'])
        dict = {"userid": userid,"qid": myList[3], "q1": myList[4], "q2": myList[0], "q3": myList[1], "q4": myList[2],"total": total}
        flash(f"You scored {total} out of 100")
        current_app.logger.info(json.dumps(dict))
        return json.dumps(dict)
        # return redirect('home')
    else:
        return redirect("login")

@home_bp.route("/profile")
def profile():
    mycursor=mydb.cursor()
    if 'userid' in session:
        userid = session['userid']
        mycursor.execute("select * from Student where id = '" + str(userid) + "' ")
        r = mycursor.fetchall()
        fname = r[0][1]
        lname = r[0][2]
        email = r[0][3]
        grade = r[0][6]
        dob = r[0][5]
        context ={'fname':fname,'lname':lname,'email':email,'grade':grade,'dob':dob}
        dict = {"userid": session['userid'], "message": "Profile Page"}
        current_app.logger.info(json.dumps(dict))
        return render_template('UserScore.html',context=context)
    else:
        return redirect("login")

@home_bp.route("/EditUserScore")
def EditUserScore():
    mycursor=mydb.cursor()
    if 'userid' in session:
        userid = session['userid']
        mycursor.execute("select * from Student where id = '" + str(userid) + "' ")
        r = mycursor.fetchall()
        fname = r[0][1]
        lname = r[0][2]
        email = r[0][3]
        grade = r[0][6]
        dob = r[0][5]
        context ={'fname':fname,'lname':lname,'email':email,'grade':grade,'dob':dob}
        return render_template('EditUserScore.html',context=context)
    else:
        return redirect("login")

@home_bp.route("/EditUserScore", methods=['POST'])
def EditUserScores():
    if request.method == 'POST':
        if 'userid' in session:
            userid = session['userid']
        fname = request.form['fname']
        lname = request.form['lname']
        email = request.form['email']
        grade = request.form['grade']
        # dob = request.form['dob']
        mycursor=mydb.cursor()
        mycursor.execute("update student set first_name='" + fname + "',last_name='" + lname +"',email='" + email +"',grade='"+grade+"' where id='" +str(userid)+"' ")
        mydb.commit()
        mycursor.close()
        return redirect('profile')
        # else:
        #     return redirect('login')

@home_bp.route("/getTime",methods=["GET"])
def getTime():
    time = request.args.get('time')
    hint_count = request.args.get('hint_count')
    quesid = request.args.get('quesid')
    dict = {"userid": session['userid'], "qid": quesid, "hint_no": hint_count}
    current_app.logger.info(json.dumps(dict))
    return "TimeReceived"

@home_bp.route("/endTime", methods=["GET"])
def endTime():
    qcount = request.args.get('qcount')
    qid = request.args.get('quesid')
    dict = {"userid": session['userid'], "qid": qid, "qcount": qcount, "message": "End"}
    current_app.logger.info(json.dumps(dict))
    return "TimeReceived"

@home_bp.route('/logout')
def logout():
    dict = {"userid": session['userid'], "message": "Logged out"}
    current_app.logger.info(json.dumps(dict))
    session.pop('userid',None)
    return redirect('/')
