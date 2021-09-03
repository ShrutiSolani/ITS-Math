from flask import Blueprint, render_template, request, flash, redirect, url_for, session, Flask, current_app
import json, os, random
from werkzeug.security import generate_password_hash , check_password_hash

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
        mycursor.execute("select * from Student where email='" + email + "' ")
        r = mycursor.fetchall()
        count = mycursor.rowcount
        mydb.commit()
        mycursor.close()
        if (count == 1):
            if check_password_hash(r[0][4],password):
                session['userid'] = r[0][0]
                dict = {"userid": session['userid'], "message": "Logged In"}
                current_app.logger.info(json.dumps(dict))
                return redirect('home')
            else:
                flash("Invalid Credentials",'danger')
                return redirect('login')    
        else:
            flash("Invalid Credentials",'danger')
            return redirect('login')




@home_bp.route("/signup")
def signup():
    dict = {"message": "Signup Page"}
    current_app.logger.info(json.dumps(dict))
    return render_template('signup.html')

@home_bp.route("/signup",methods=['POST'])
def signups():
    mycursor=mydb.cursor()

    if request.method=="POST":
        fname = request.form['fname']
        lname = request.form['lname']
        email = request.form['email']
        password = request.form['password']
        cpassword = request.form['cpassword']
        dob = request.form['dob']
        grade=request.form['grade']

        mycursor.execute("select * from Student where email='" + email + "' ")
        r = mycursor.fetchall()
        count = mycursor.rowcount
        mydb.commit()
        mycursor.close()
        if count == 1:
            flash("User with that email already exist",'danger')
            return redirect('signup')

        if password != cpassword:
            flash("Both Password didn't match.",'danger')
            return redirect('signup')

        hashed_password = generate_password_hash(password)

        mycursor=mydb.cursor()
        mycursor.execute("Insert into Student(first_name,last_name,email,password,dob,grade)values(%s,%s,%s,%s,%s,%s)",(fname,lname,email,hashed_password,dob,grade))
        mydb.commit()
        mycursor.close()
        flash("User created succesfully.",'success')
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
    mycursor=mydb.cursor()
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
        qids = myList[3]
        mycursor.execute("select * from Question where qid='" + qids + "' ")
        r = mycursor.fetchall()
        qid = r[0][0]
        userid = session['userid']
        mycursor.execute("select * from Student where id='" + str(userid) + "' ")
        rs= mycursor.fetchall()
        uid = rs[0][0]
        # mycursor.execute("Insert into Student(first_name,last_name,email,password,dob,grade)values(%s,%s,%s,%s,%s,%s)",(fname,lname,email,hashed_password,dob,grade))
        mycursor.execute("INSERT INTO Student_Score(sid,qid,score)values(%s,%s,%s)",(uid,qid,total))
        
        # querys = "INSERT INTO Student_Score(sid,qid,score)values(%d,%d,%d)",(userid,qid,total)
        # mycursor.execute(querys)
        mydb.commit()
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
        school = r[0][7]
        context ={'fname':fname,'lname':lname,'school':school,'email':email,'grade':grade,'dob':dob}
        dict = {"userid": session['userid'], "message": "Profile Page"}
        current_app.logger.info(json.dumps(dict))

        mycursor.execute("select * from Student where id='" + str(userid) + "' ")
        rs= mycursor.fetchall()
        uid = rs[0][0]

        mycursor.execute("select distinct qid , score from Student_Score where sid='" + str(userid) + "' ")
        r2= mycursor.fetchall()
        
        AE = 0
        AI = 0
        FE = 0
        FI = 0
        algebra= {}
        fraction = {}
        for i in r2:
            qid = i[0]
            mycursor.execute("select * from Question where id='" + str(qid) + "' ")
            r3= mycursor.fetchall()
            chapter = r3[0][2]
            level = r3[0][3]
            topic = r3[0][4]
            if level == "Easy" and chapter == "Algebra":
                AE+=1
                algebra[topic] = i[1]
            elif level == "Easy" and chapter == "Fraction":
                FE+=1
                fraction[topic] = i[1]
            elif level == "Intermediate" and chapter == "Algebra":
                AI+=1
                algebra[topic] = i[1]
            elif level == "Intermediate" and chapter == "Fraction":
                FI+=1
                fraction[topic] = i[1]
        context2 = {'AE':AE,'AI':AI,'FE':FE,'FI':FI}


        return render_template('UserScore.html',context=context,context2=context2,algebra=algebra,fraction=fraction)
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
        school = r[0][7]
        context ={'fname':fname, 'school':school,'lname':lname,'email':email,'grade':grade,'dob':dob}
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
        school = request.form['school']
        # dob = request.form['dob']
        mycursor=mydb.cursor()
        mycursor.execute("update student set first_name='" + fname + "',last_name='" + lname +"',email='" + email +"',grade='"+grade+"',school='"+school+"'  where id='" +str(userid)+"' ")
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
