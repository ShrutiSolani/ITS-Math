from flask import Blueprint, render_template, request, flash, redirect, url_for, session, current_app
import os, json, random, datetime, math
from fractions import Fraction

SITE_ROOT = os.path.realpath(os.path.dirname(__file__))


json_url = os.path.join(SITE_ROOT, "static/data", "qid.json")
data = json.load(open(json_url))
datetimes = []
count=0

fractions_bp = Blueprint("fractions_bp", __name__, template_folder = "templates", static_folder="static")

startTym=datetime.datetime.now()


@fractions_bp.route("/divide_with_whole")
def divide_with_whole():
    global count
    global datetimes
    global startTym
    startTym=datetime.datetime.now()
    qid = data["divide-with-whole"]
    num=random.randint(2,30)
    den=random.randint(2,20)
    div=random.randint(2,10)

    que="Divide this "+"("+str(num)+"/"+str(den)+") by a whole number "+str(div)+"."
    numerator=num
    denominator=den*div

    frac=Fraction(numerator=numerator , denominator=denominator)
    ans_num=frac.numerator
    ans_den=frac.denominator

    h1 = "Rearrange into like terms (coefficients with same variable and power)"
    h2 = "Add coefficientts of like terms"
    h3 = "Solution : " + str(ans_num)+ "/" + str(ans_den)
    hints = {"h1": h1, "h2": h2, "h3": h3}
    context={"qid": qid,"que":que,"numerator":numerator,"hints":hints,"denominator":denominator,"ans_num":ans_num,"ans_den":ans_den,"rec_num":1,"rec_den":div}
    scoredict = {"score": "", "total": "", "totalqts": "", "pct": ""}
    count+=1
    dict = {"userid": session['userid'], "qid": qid, "qcount": count}
    current_app.logger.info(json.dumps(dict))

    return render_template("divideby_whole.html",answer=context)


@fractions_bp.route("/multiply-with-whole")
def multiply_with_whole():
    global count
    global datetimes
    global startTym
    startTym=datetime.datetime.now()
    qid = data["multiply-with-whole"]
    q=[]
    ans_num=[]
    ans_den=[]
    for i in range(2):
        num = random.randint(1,10)
        den = random.randint(2,25)
        wh = random.randint(1,10)
        que = "Multiply Fraction "+ str(num) + "/" + str(den) + " by whole number " + str(wh)
        ansnum = num*wh
        ansden = den
        ans_num.append(ansnum)
        ans_den.append(ansden)
        q.append(que)
    q.insert(1," ")
    count+=1
    dict = {"userid": session['userid'], "qid": qid, "qcount": count}
    current_app.logger.info(json.dumps(dict))

    return render_template("division.html",easy={"num": 2,"topic": "Multiple by Whole number","ans_num":ans_num,"ans_den":ans_den,"q":q, "label1": "Numerator", "label2": "Denominator", "qid": qid})


@fractions_bp.route("/add-fractions")
def add_fractions():
    global count
    global datetimes
    global startTym
    startTym=datetime.datetime.now()
    qid = data["add-fractions"]
    q=[]
    ans_num=[]
    ans_den=[]
    for i in range(2):
        num1=random.randint(1,25)
        den=random.randint(2,10)
        num2=random.randint(1,25)

        qs="Add this two fractions "+str(num1)+"/"+str(den)+" and "+str(num2)+"/"+str(den)+"."
        ansnum=num1+num2
        ansden=den
        ans_num.append(ansnum)
        ans_den.append(ansden)
        q.append(qs)
    q.insert(1," ")
    contexts={"num": 1,"qid": qid,"topic": "Add like fractions","ans_num":ans_num,"ans_den":ans_den,"q":q, "label1": "Numerator", "label2" : "Denominator"}
    count+=1
    dict = {"userid": session['userid'], "qid": qid, "qcount": count}
    current_app.logger.info(json.dumps(dict))

    return render_template("division.html",easy=contexts)


@fractions_bp.route("/division")
def division():
    global count
    global datetimes
    global startTym
    startTym=datetime.datetime.now()
    qid = data["division"]
    q=[]
    ans_num=[]
    ans_den=[]
    for i in range(2):
        num=random.randint(1,50)
        den=random.randint(2,10)
        qs="Find quotient and remainder of "+str(num)+"/"+str(den)+"."
        ansnum=(num//den)
        ansden=(num%den)
        q.append(qs)
        ans_num.append(ansnum)
        ans_den.append(ansden)
    q.insert(1," ")
    easy={"ans_num":ans_num,"ans_den":ans_den,"q":q, "label1": "Quotient", "label2": "Remainder", "qid": qid}
    count+=1
    dict = {"userid": session['userid'], "qid": qid, "qcount": count}
    current_app.logger.info(json.dumps(dict))

    return render_template("division copy.html",easy=easy)


@fractions_bp.route("/unlike-add")
def unlike_add():
    global count
    global datetimes
    global startTym
    startTym=datetime.datetime.now()
    qid = data["unlike-add"]
    num1=random.randint(2,50)
    den1=random.randint(2,20)
    num2=random.randint(2,50)
    den2=random.randint(2,20)
    sign=["+","-"]
    q=["Add","Subtract"]
    while(den1==den2):
        random.randint(2,20)
    if(random.choice(sign) == "+"):
        que = q[0] + " (" + str(num1) + "/" + str(den1) + ") by " + "(" + str(num2) + "/" + str(den2) + ")" + "."
        numerator1=num1
        denominator1=den1
        numerator2 = num2
        denominator2 = den2

        frac1=Fraction(numerator1,denominator1)
        drac2=Fraction(numerator2,denominator2)

        num_ans=(numerator1*denominator2) + (numerator2*denominator1)
        den_ans=denominator1*denominator2
        ans_frac=Fraction(num_ans,den_ans)
        opsign='+'
    else:
        que = q[1] + " (" + str(num2) + "/" + str(den2) + ") by " + "(" + str(num1) + "/" + str(den1) + ")" + "."
        numerator1 = num1
        denominator1 = den1
        numerator2 = num2
        denominator2 = den2

        frac1 = Fraction(numerator1, denominator1)
        drac2 = Fraction(numerator2, denominator2)

        num_ans = (numerator1 * denominator2) - (numerator2 * denominator1)
        den_ans = denominator1 * denominator2
        ans_frac = Fraction(num_ans, den_ans)
        opsign='-'


    answer = {"qid": qid,"que": que, "num_ans": ans_frac.numerator, "den_ans": ans_frac.denominator, "den": den_ans, "num": num_ans,"num1":num1,"den1":den1,"num2":num2,"den2":den2,"q":que,"opsign":opsign}
    count+=1
    dict = {"userid": session['userid'], "qid": qid, "qcount": count}
    current_app.logger.info(json.dumps(dict))

    return render_template("Fraction_operation.html", answer=answer)


@fractions_bp.route("/simplest-form")
def simplest_form():
    global count
    global datetimes
    global startTym
    startTym=datetime.datetime.now()
    qid = data["simplest-form"]
    num = random.randint(1,50)
    den = random.randint(2,50)
    que = "Find simplest form of fraction "+ str(num)+"/"+ str(den)
    simple = Fraction(num, den)
    answer = {"que": que, "num_ans": simple.numerator, "den_ans": simple.denominator}
    easy = {"topic": "Simplest Form", "qid": qid}
    userid = session["userid"]
    count+=1
    dict = {"userid": session['userid'], "qid": qid, "qcount": count}
    current_app.logger.info(json.dumps(dict))

    return render_template("simplestForm.html",answer=answer, easy = easy)


@fractions_bp.route("/normal-form")
def mixed_to_normal():
    global count
    global datetimes
    global startTym
    startTym=datetime.datetime.now()
    qid = data["normal-form"]
    num = random.randint(1,50)
    den = random.randint(2,50)
    whole = random.randint(2,20)
    que = "Convert "+str(whole)+" ("+str(num)+"/"+str(den)+") to normal form and find simplest form"
    num_ans = (den*whole)+num
    frac = Fraction(num_ans,den)
    answer = {"qid": qid,"que":que, "num_ans":frac.numerator, "den_ans":frac.denominator,"den":den,"num":num_ans}
    count+=1
    dict = {"userid": session['userid'], "qid": qid, "qcount": count}
    current_app.logger.info(json.dumps(dict))

    return render_template("Normal_form.html", answer=answer)


@fractions_bp.route("/mixed-fraction")
def question():
    global count
    global datetimes
    global startTym
    startTym=datetime.datetime.now()
    # if len(datetimes)==4:
    #     datetimes=[]
    # datetimes.append(x)

    qid = data["mixed-fraction"]
    num = random.randint(1, 100)
    den = random.randint(1, 25)
    while num < den:
        num = random.randint(1, 100)
    que = "Express as mixed fraction : " + str(num) + "/" + str(den) + "."
    quo = num // den
    rem = num % den
    box_ans = [quo, rem, quo, rem, den]
    answer = {"qid": qid, "que": que, "b0": box_ans[0], "b1": box_ans[1], "b2": box_ans[2], "b3": box_ans[3], "b4": box_ans[4]}
    count+=1
    dict = {"userid": session['userid'], "qid": qid, "qcount": count}
    current_app.logger.info(json.dumps(dict))
    return render_template("Mixed_fraction.html", answer=answer)


def LCM(a, b):
        return abs(a * b) // math.gcd(a, b)


@fractions_bp.route("/compare")
def compare():
    global count
    global datetimes
    global startTym
    startTym=datetime.datetime.now()
    qid = data["compare"]
    num1 = random.randint(1,100)
    den1 = random.randint(2,25)
    num2 = random.randint(1, 100)
    den2 = random.randint(2, 25)
    f1 = Fraction(num1,den1)
    f2 = Fraction(num2,den2)
    que = "Compare "+str(f1)+" and "+str(f2)+" . "
    lcm = LCM(f1.denominator,f2.denominator)
    eqfrac1 = lcm//den1
    eqfrac2 = lcm//den2
    num1 = num1*eqfrac1
    den1 = den1*eqfrac1
    num2 = num2*eqfrac2
    den2 = den2*eqfrac2
    fract1=Fraction(num1,den1)
    fract2=Fraction(num2,den2)
    if(fract1>fract2):
        ans="1"
    elif fract2>fract1:
        ans="2"
    else:
        ans="3"
    answer={"qid": qid, "que":que,"lcm":lcm,"num1":num1,"den1":den1,"num2":num2,"den2":den2,"ans":ans , "f1":f1,"f2":f2}
    count+=1
    dict = {"userid": session['userid'], "qid": qid, "qcount": count}
    current_app.logger.info(json.dumps(dict))

    return render_template("fracompare.html", answer=answer)
