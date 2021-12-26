from datetime import datetime
from flask import Blueprint, render_template, request, flash, redirect, url_for, session, Flask, current_app
import json, os, random

from ..fractions1 import routes
from ..algebra import routes
from werkzeug.security import generate_password_hash, check_password_hash

from ..database import mydb

# import mysql.connector
# mydb = mysql.connector.connect(
#     host = "sql6.freesqldatabase.com",
#     user = "sql6449635",
#     database = "sql6449635",
#     password ="EH7dFtDVqR",
#     port = "3306"
# )


home_bp = Blueprint('home_bp', __name__, template_folder = 'templates', static_folder='static')

def log_entry(dict):
    try:
        current_app.logger.info(json.dumps(dict))
        mycursor=mydb.cursor()
        sql = "Insert into log(entry)values('%s')" %(dict)
        mycursor.execute(sql)
        mydb.commit()
        mycursor.close()
    except Exception as e:
        mycursor.close()
        print(e)
    finally:
        return "Success"



@home_bp.route('/')
def index():
    return render_template('index.html')

@home_bp.route('/copy')
def copy():
    return render_template('home-copy.html',name={'name':'raj'})

@home_bp.route("/login")
def login():
    return render_template('login.html')

@home_bp.route("/logins",methods=['POST'])
def logins():

    mycursor=mydb.cursor()
    if request.method=='POST':
        email=request.form['email']
        password=request.form['password']
        mycursor.execute("select * from student where email='" + email + "' ")
        r = mycursor.fetchall()
        count = mycursor.rowcount
        mydb.commit()
        mycursor.close()
        if (count == 1):
            if check_password_hash(r[0][4],password):
                session['userid'] = r[0][0]
                dict = {"userid": session['userid'], "message": "Logged In"}
                log_entry(json.dumps(dict))
                return redirect('home')
            else:
                flash("Invalid Credentials",'danger')
                return redirect('login')
        else:
            flash("Invalid Credentials",'danger')
            return redirect('login')




@home_bp.route("/signup")
def signup():
    return render_template('signup.html')

@home_bp.route("/signup",methods=['POST'])
def signups():
    print("in signups")
    mycursor=mydb.cursor()

    if request.method=="POST":
        fname = request.form['fname']
        lname = request.form['lname']
        email = request.form['email']
        password = request.form['password']
        cpassword = request.form['cpassword']
        dob = request.form['dob']
        grade=request.form['grade']
        print("got form data")
        mycursor.execute("select * from student where email='" + email + "' ")
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
        mycursor.execute("Insert into student(first_name,last_name,email,password,dob,grade)values(%s,%s,%s,%s,%s,%s)",(fname,lname,email,hashed_password,dob,grade))
        mydb.commit()
        mycursor.close()
        print("inserted")
        flash("User created succesfully.",'success')
        return redirect('login')
    else:
        print("else")
        return redirect('signup')

@home_bp.route("/home")
def home():
    mycursor=mydb.cursor()
    if 'userid' in session:
        mycursor.execute("select * from student where id="+str(session['userid']))
        r = mycursor.fetchall()
        dict = {"userid": session["userid"], "message": "Home Page"}
        log_entry(json.dumps(dict))
        return render_template('home.html',name={'name':r[0][1]})
    else:
        return redirect('login')

@home_bp.route('/score', methods=['POST'])
def score():
    mycursor=mydb.cursor()
    if request.method == 'POST':
        if 'userid' in session:
            userid=session['userid']
        tup = request.get_json('data')
        myList = list(tup.values())
        total = int(tup['undefined']) + int(tup['1']) + int(tup['2']) + int(tup['3'])
        dict = {"userid": userid,"qid": myList[3], "q1": myList[4], "q2": myList[0], "q3": myList[1], "q4": myList[2],"total": total}
        flash(f"You scored {total} out of 100")
        log_entry(json.dumps(dict))
        qids = myList[3]
        mycursor.execute("select * from question where qid='" + qids + "' ")
        r = mycursor.fetchall()
        qid = r[0][0]
        userid = session['userid']
        mycursor.execute("select * from student where id='" + str(userid) + "' ")
        rs= mycursor.fetchall()
        uid = rs[0][0]
        # mycursor.execute("Insert into student(first_name,last_name,email,password,dob,grade)values(%s,%s,%s,%s,%s,%s)",(fname,lname,email,hashed_password,dob,grade))
        mycursor.execute("INSERT INTO student_score(sid,qid,score)values(%s,%s,%s)",(uid,qid,total))

        # querys = "INSERT INTO student_score(sid,qid,score)values(%d,%d,%d)",(userid,qid,total)
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
        mycursor.execute("select * from student where id = '" + str(userid) + "' ")
        r = mycursor.fetchall()
        fname = r[0][1]
        lname = r[0][2]
        email = r[0][3]
        grade = r[0][6]
        dob = r[0][5]
        school = r[0][7]
        context ={'fname':fname,'lname':lname,'school':school,'email':email,'grade':grade,'dob':dob}
        dict = {"userid": session['userid'], "message": "Profile Page"}
        log_entry(json.dumps(dict))

        mycursor.execute("select * from student where id='" + str(userid) + "' ")
        rs= mycursor.fetchall()
        uid = rs[0][0]

        mycursor.execute("select distinct qid , score from student_score where sid='" + str(userid) + "' ")
        r2= mycursor.fetchall()

        AE = 0
        AI = 0
        FE = 0
        FI = 0
        algebra= {}
        fraction = {}
        for i in r2:
            qid = i[0]
            mycursor.execute("select * from question where id='" + str(qid) + "' ")
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
        mycursor.execute("select * from student where id = '" + str(userid) + "' ")
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
    log_entry(json.dumps(dict))
    return "TimeReceived"

@home_bp.route("/endTime", methods=["GET"])
def endTime():
    print("In endTime")
    mycursor=mydb.cursor()
    print(263)
    qcount = request.args.get('qcount')
    print(265)
    qid = request.args.get('quesid')
    print(267)
    hcount =request.args.get('hcount')
    print(269)
    htime = json.loads(request.args.get('htime'))
    print(271)
    score = request.args.get('score')
    print(273)
    try:
        startTym = routes.startTym
    except Exception as e:
        print(e)
    print(275)
    try:
        endTym = datetime.now()
    except Exception as e:
        print(e)
    print(277)
    wrong = request.args.get('wrong')
    print(279)
    wronghint = request.args.get('wronghint')
    print(281)
    print("before query ")
    mycursor.execute("select * from question where qid = '" + str(qid) + "' ")
    print("after query ")
    r = mycursor.fetchall()
    chapter = r[0][2]
    lod = r[0][3] #Level Of Difficulty
    if(len(htime)==1):
        hintTime1 = datetime.fromtimestamp(htime[0]/1000)
        hintTime2 = 0
    elif(len(htime)==2):
        hintTime1 = datetime.fromtimestamp(htime[0]/1000)
        hintTime2 = datetime.fromtimestamp(htime[1]/1000)
    else:
        hintTime1 = 0
        hintTime2 = 0
    endhtym1=0
    endhtym2=0
    if(hintTime1!=0):
        endhtym1 = endTym - hintTime1
        if(hintTime2!=0):
            tyms = hintTime2
        else:
            tyms=endTym
        difference = tyms-hintTime1
    if(hintTime2!=0):
        endhtym2 = endTym - hintTime2
    # totalTym = endhtym1 + endhtym2
    print("After data")
    dict = {"userid": session['userid'], "qid": qid, "qcount": qcount, "startTime" : startTym, "endTime" : endTym, "levelofdifficulty":lod,"chapter":chapter,"hintCount" : hcount, "h1time":hintTime1,"h2time":hintTime2,"diffh1":endhtym1,"diffh2":endhtym2,"wrongCount":wrong,"wronghintcount":wronghint,"score":score}
    print(dict)
    log_entry(json.dumps(dict,default=str))
    print("After log")
    return "TimeReceived"


@home_bp.route('/logout')
def logout():
    dict = {"userid": session['userid'], "message": "Logged out"}
    log_entry(json.dumps(dict))
    session.pop('userid',None)
    return redirect('/')
