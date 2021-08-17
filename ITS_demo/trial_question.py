import re
from flask import Flask, render_template, request, flash, redirect, url_for, session
# from flask_login import current_user
from fractions import Fraction
import random, os, math, json, logging
import mysql.connector
import datetime

app = Flask(__name__)

logging.basicConfig(filename = 'UserLog.csv', level=logging.INFO, format = '%(message)s')
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)
file1=logging.basicConfig(filename = 'UserActivity.log', level=logging.INFO, format = '%()%(message)s')
Image_folder = os.path.join('static', 'images')

app.config['UPLOAD_FOLDER'] = Image_folder
full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'cross.jpg')


SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
json_url = os.path.join(SITE_ROOT, "static/data", "qid.json")
data = json.load(open(json_url))

mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="ITS"
    )

@app.route("/")
def index():
    # app.logger.info('Index Page')
    return render_template('index_new.html')


@app.route("/login")
def login():
    # app.logger.info('Login Page')
    return render_template('login_new.html')

@app.route("/login",methods=['POST'])
def logins():
    
    mycursor=mydb.cursor()
    if request.method=='POST':
        email=request.form['email']
        password=request.form['password']
        mycursor.execute("select * from Student where email='" + email + "' and password='" + password + "'")
        r = mycursor.fetchall()
        # print(r[0][0])
        count = mycursor.rowcount
        if (count == 1):
            session['userid'] = r[0][0]
            return redirect(url_for('home'))
        else:
            return redirect(url_for('logins'))
    mydb.commit()
    mycursor.close()

@app.route("/signup")
def signup():
    # app.logger.info('Signup Page')
    return render_template('signup_new.html')

@app.route("/signup",methods=['POST'])
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

        mycursor.execute("Insert into Student(first_name,last_name,email,password,dob,grade)values(%s,%s,%s,%s,%s,%s)",(fname,lname,email,password,dob,grade))
        mydb.commit()
        mycursor.close()
        return redirect('login')
    else:
        return redirect('signup')

@app.route("/home")
def home():
    # app.logger.info('Home Page')
    mycursor=mydb.cursor()
    if 'userid' in session:
        mycursor.execute("select * from Student where id="+str(session['userid']))
        r = mycursor.fetchall()
        return render_template('home_new.html',name={'name':r[0][1]})
    else:
        return redirect(url_for('login'))


@app.route('/score', methods=['POST'])
def score():
    if request.method == 'POST':
        if 'userid' in session:
            print(session['userid'])
            userid=session['userid']
        now = datetime.datetime.now()
        tup = request.form
        # print(tup)
        total = int(tup['data[1]']) + int(tup['data[2]']) +int(tup['data[3]']) +int(tup['data[undefined]']) 
        print(total)
        # print(type(userid))
        # userid , timestamp , event ,qid ,ts1, sq1, Ets1 ,ts2, sq2, Ets2 ,ts3, sq3, Ets3 ,ts4, sq4, Ets4 
        app.logger.info('%d,%s,%s,%d,%s,%s,%d,%s,%s,%d,%s,%s,%d,%s',int(userid),str(tup['data[qid]']),str(datetimes[0]),int(tup['data[undefined]']),str(datetimes[1]),str(datetimes[1]),int(tup['data[1]']),str(datetimes[2]),str(datetimes[2]),int(tup['data[2]']),str(datetimes[3]),str(datetimes[3]),int(tup['data[3]']),str(now))
        return "Score received"
    else:
        return redirect(url_for("login"))

@app.route("/profile")
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
        return render_template('UserScore.html',context=context)
    else:
        return redirect(url_for("login"))

@app.route("/mixed-fraction")
def question():
    qid = data['mixed-fraction']
    num = random.randint(1, 100)
    den = random.randint(1, 25)
    while num < den:
        num = random.randint(1, 100)
    que = 'Express as mixed fraction : ' + str(num) + '/' + str(den) + '.'
    quo = num // den
    rem = num % den
    box_ans = [quo, rem, quo, rem, den]
    answer = {'qid': qid, 'que': que, 'b0': box_ans[0], 'b1': box_ans[1], 'b2': box_ans[2], 'b3': box_ans[3], 'b4': box_ans[4]}
    return render_template('Mixed_fraction.html', easy=answer)


def LCM(a, b):
        return abs(a * b) // math.gcd(a, b)


@app.route("/compare")
def compare():
    qid = data['compare']
    num1=random.randint(1,100)
    den1=random.randint(2,25)
    num2 = random.randint(1, 100)
    den2 = random.randint(2, 25)
    f1= Fraction(num1,den1)
    f2= Fraction(num2,den2)
    que = "Compare "+str(f1)+" and "+str(f2)+" . "
    lcm=LCM(f1.denominator,f2.denominator)
    eqfrac1=lcm//den1
    eqfrac2=lcm//den2
    num1=num1*eqfrac1
    den1=den1*eqfrac1
    num2 = num2 * eqfrac2
    den2 = den2 * eqfrac2
    fract1=Fraction(num1,den1)
    fract2=Fraction(num2,den2)
    if(fract1>fract2):
        ans="1"
    elif fract2>fract1:
        ans="2"
    else:
        ans="3"
    answer={'qid': qid, 'que':que,'lcm':lcm,'num1':num1,'den1':den1,'num2':num2,'den2':den2,'ans':ans , 'f1':f1,'f2':f2}
    return render_template('fracompare.html', answer=answer)


datetimes=[]

@app.route("/algebra-add")
def horizontal_add():
    # print("appp")
    global datetimes
    x=datetime.datetime.now()
    if len(datetimes)==4:
        datetimes=[]
    datetimes.append(x)
    
    qid = data['algebra-add']
    coeff = random.sample(range(-50,50),6) 
    varx = ['x','x\u00b2','x\u00b3'] 
    vary = ['y','y\u00b2','y\u00b3'] 
    rx = random.choice(varx)
    ry = random.choice(vary)
    sign = []
    for i in coeff[1:6:2]:
        if i < 0:
            sign.append('')
        else:
            sign.append('+')

    haddque = 'Add horizontally '+str(coeff[0])+rx+sign[0]+str(coeff[1])+ry+','+str(coeff[2])+rx+sign[1]+str(coeff[3])+ry+','+str(coeff[4])+rx+sign[2]+str(coeff[5])+ry
    x_like = coeff[0:5:2]
    x_sum = sum(x_like)
    y_like = coeff[1:6:2]
    y_sum = sum(y_like)
    answer = {'qid': qid, 'que':haddque,'varx':rx,'vary':ry,'coeff':coeff,'x_like':x_like,'y_like':y_like,'x_sum':x_sum,'y_sum':y_sum}
    return render_template('algebra_add.html', answer=answer)


@app.route('/vertical_sub')
def vertical_sub():
    qid = data['vertical-sub']
    coeff = random.sample(range(-50, 50), 6)  
    varx = ['x', 'x\u00b2', 'x\u00b3']  
    vary = ['y', 'y\u00b2', 'y\u00b3']  
    varz = ['z', 'z\u00b2', 'z\u00b3'] 
    rx = random.choice(varx)
    ry = random.choice(vary)
    rz = random.choice(varz)
    sign_1 = []
    for i in coeff[1:3]:
        if i < 0:
            sign_1.append('')
        else:
            sign_1.append('+')
    sign_2=[]
    for j in coeff[4:7]:
        if(j<0):
            sign_2.append("")
        else:
            sign_2.append('+')
    haddque = 'Sub Vertically ' + str(coeff[0])+rx+str(sign_1[0])+str(coeff[1])+ry+str(sign_1[1])+str(coeff[2])+rz+' , '+str(coeff[3])+rx+str(sign_2[0])+str(coeff[4])+ry+str(sign_2[1])+str(coeff[5])+rz+' . '
    x_diff = coeff[0] - coeff[3]
    y_diff = coeff[1] - coeff[4]
    z_diff = coeff[2] - coeff[5]
    answer = {'qid': qid, 'que': haddque, 'varx': rx, 'vary': ry,'varz':rz,'coeff': coeff,'x_diff': x_diff, 'y_diff': y_diff,'z_diff':z_diff}
    return render_template('vertical_sub.html', answer=answer)

@app.route('/simplest-form')
def simplest_form():
    qid = data['simplest-form']
    num = random.randint(1,50)
    den = random.randint(2,50)
    que = "Find simplest form of fraction "+ str(num)+"/"+ str(den)
    simple = Fraction(num, den)
    answer = {'que': que, 'num_ans': simple.numerator, 'den_ans': simple.denominator}
    easy = {'topic': 'Simplest Form', 'qid': qid}
    return render_template('simplestForm.html',answer=answer, easy = easy)


#simplest_form()

#mixed to normal form
@app.route('/normal-form')
def mixed_to_normal():
    qid = data['normal-form']
    num = random.randint(1,50)
    den = random.randint(2,50)
    whole = random.randint(2,20)
    que = "Convert "+str(whole)+" ("+str(num)+"/"+str(den)+") to normal form and find simplest form"
    num_ans = (den*whole)+num
    frac = Fraction(num_ans,den)
    answer = {'qid': qid,'que':que, 'num_ans':frac.numerator, 'den_ans':frac.denominator,'den':den,'num':num_ans}
    return render_template('Normal_form.html', answer=answer)
    

@app.route('/unlike-add')
def unlike_add():
    qid = data['unlike-add']
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


    answer = {'qid': qid,'que': que, 'num_ans': ans_frac.numerator, 'den_ans': ans_frac.denominator, 'den': den_ans, 'num': num_ans,'num1':num1,'den1':den1,'num2':num2,'den2':den2,'q':que}
    return render_template('Fraction_operation.html', answer=answer)


@app.route('/value-of-expression')
def value_of_expression():
    qid = data['value-of-expression']
    cnt=0
    variable=["","p","p\u00b2","p\u00b3"]
    sign = ["+", "-"]
    terms = []
    answers = []
    num=random.randint(2,10)
    q4 = "If p = "+str(num)+", find the value of "
    while(cnt<4):   
        c1 =  random.randint(1,10) 
        c2 =  random.randint(1,10) 
        c3 =  random.randint(1,10) 
        s1 = random.choice(sign)
        s2 = random.choice(sign)
        v1 = random.choice(variable)
        v2 = random.choice(variable)
        v3 = random.choice(variable)
        term = str(c1) + str(v1) + str(s1) + str(c2) + str(v2) + str(s2) + str(c3) + str(v3)
        i1=find_term(v1,variable)
        i2=find_term(v2,variable)
        i3=find_term(v3,variable)
        var1=num**i1
        var2=num**i2
        var3=num**i3
        if(s1 == "+" and s2=="+"):
            answer =  c1*var1 + c2*var2 + c3*var3
        elif(s1=="+" and s2=="-"):
            answer= c1*var1 + c2*var2 - c3*var3
        elif(s1=="-" and s2=="-"):
            answer= c1*var1 - c2*var2 - c3*var3
        elif(s1=="-" and s2=="+"):
            answer= c1*var1 - c2*var2 + c3*var3 
        terms.append(term)      
        answers.append(answer) 
        cnt += 1

    return render_template('algebra_easy.html', easy={'topic': 'Value of Expression','question': q4, 'options': terms, 'answer': answers, 'num': 2, 'qid': qid})
        
def find_term(v, a):
    return a.index(v)


@app.route('/coefficient')
def coefficient():
    qid = data['coefficient']
    q1 = 'Identify the numerical coefficients of terms (other than constants) in the following expressions'
    variable = ["x", "x\u00b2", "x\u00b3"]
    sign = ["+", "-"]
    terms = []
    answers = []
    count = 0
    while count <= 3:
        coeff = random.randint(1, 10)
        num = random.randint(1,30)
        var = random.choice(variable)
        op = random.choice(sign)
        term = str(num) + op + str(coeff) + random.choice(variable)
        terms.append(term)
        if(op == "-"):
            answers.append(-coeff)
        else:
            answers.append(coeff)
        count += 1
    return render_template('algebra_easy.html', easy={'topic': 'Identifying Coefficient','question': q1, 'options': terms, 'answer': answers, 'num': 1, 'qid': qid})


@app.route('/monomial')
def monomial():
    qid = data['monomial']
    terms2 = ['2y + 14z', '20', 'a\u00b2 + b\u00b2 - 2ab', '8xy']
    q2 = 'Classify into monomials, binomials and trinomials'
    variable = ["x", "y", "z", "xy", "yz", "xz", "xyz"]
    sign = ["+", "-"]
    answers = []
    terms = []
    count = 0
    while count <= 3:
        x = random.randint(1, 3)
        answer = ""
        if x == 1:
            answer = "Monomial"
            term = str(random.randint(1, 25)) + random.choice(variable)
        elif x == 2:
            answer = "Binomial"
            term = str(random.randint(1, 25)) + random.choice(variable) + random.choice(sign) + str(random.randint(1, 25)) + random.choice(variable)
        elif x == 3:
            answer = "Trinomial"
            term = str(random.randint(1, 25)) + random.choice(variable) + random.choice(sign) + str(
                random.randint(1, 25)) + random.choice(variable) + random.choice(sign) + str(
                random.randint(1, 25)) + random.choice(variable)
        answers.append(answer)
        terms.append(term)
        count += 1

    contexts={'qid': qid, 'question': q2, 'options': terms, 'answer': answers, 'num': 1, 'topic': 'Monomial Binomial Trinomial'}
    return render_template('algebra2.html', easy=contexts)



@app.route("/like-unlike")
def like_unlike():
    qid = data['like-unlike']
    q3 = 'State whether a given pair of terms is of like or unlike terms'
    term1 = ['x', 'y', 'xy', 'xy\u00b2', 'x\u00b2y']
    term2 = ['x', 'y', 'yx', random.choice(['y\u00b2x', 'xy\u00b2']), random.choice(['yx\u00b2', 'x\u00b2y'])]
    answers = []
    terms = []
    count = 0
    while count <= 3:
        t1 = random.choice(term1)
        t2 = random.choice(term2)
        x = str(random.randint(1, 25))
        y = str(random.randint(1, 25))
        if term1.index(t1) == term2.index(t2):
            answer = "Like"
        else:
            answer = "Unlike"
        t1 = x+t1
        t2 = y+t2
        terms.append([t1, t2])
        answers.append(answer)
        count += 1
    contexts={'qid': qid, 'question': q3, 'options': terms, 'answer': answers, 'num': 2, 'topic': 'Like-Unlike Terms'}
    return render_template('algebra2.html',easy=contexts)

@app.route('/division')
def division():
    qid = data['division']
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
    easy={'ans_num':ans_num,'ans_den':ans_den,'q':q, 'label1': 'Quotient', 'label2': 'Remainder', 'qid': qid}

    return render_template('division copy.html',easy=easy)


@app.route('/add-fractions')
def add_fractions():
    qid = data['add-fractions']
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
    contexts={'num': 1,'qid': qid,'topic': 'Add like fractions','ans_num':ans_num,'ans_den':ans_den,'q':q, 'label1': 'Quotient', 'label2' : 'Remainder'}
    return render_template('division.html',easy=contexts)


@app.route('/multiply-with-whole')
def multiply_with_whole():
    qid = data['multiply-with-whole']
    q=[]
    ans_num=[]
    ans_den=[]
    for i in range(2):
        num = random.randint(1,10)
        den = random.randint(2,25)
        wh = random.randint(1,10)
        que = 'Multiply Fraction '+ str(num) + "/" + str(den) + " by whole number " + str(wh)
        ansnum = num*wh
        ansden = den
        ans_num.append(ansnum)
        ans_den.append(ansden)
        q.append(que)
    q.insert(1," ")
    return render_template('division.html',easy={'num': 2,'topic': 'Multiple by Whole number','ans_num':ans_num,'ans_den':ans_den,'q':q, 'label1': 'Numerator', 'label2': 'Denominator', 'qid': qid})

@app.route('/divide-with-whole')
def divide_with_whole():
    qid = data['divide-with-whole']
    num=random.randint(2,30)
    den=random.randint(2,20)
    div=random.randint(2,10)

    que="Divide this "+"("+str(num)+"/"+str(den)+") by a whole number "+str(div)+"."
    numerator=num
    denominator=den*div

    frac=Fraction(numerator=numerator , denominator=denominator)
    ans_num=frac.numerator
    ans_den=frac.denominator

    h1 = 'Rearrange into like terms (coefficients with same variable and power)'
    h2 = 'Add coefficientts of like terms'
    h3 = 'Solution : ' + str(ans_num)+ '/' + str(ans_den)
    hints = {'h1': h1, 'h2': h2, 'h3': h3}
    context={'qid': qid,'que':que,'numerator':numerator,'hints':hints,'denominator':denominator,'ans_num':ans_num,'ans_den':ans_den,'rec_num':1,'rec_den':div}
    scoredict = {'score': "", 'total': "", 'totalqts': "", 'pct': ""}
    return render_template('divideby_whole.html',answer=context)


@app.route('/fraction-intermediate')
def fraction_intermediate():
    full={'f1':{'q1':'Expressed as Mixed Fraction','h1':'Mixed Fraction','link':'/mixed-fraction'},
    'f2':{'q1':'Compare Two Fraction','h1':'Compare','link':'/compare'},
    'f3':{'q1':'Convert Mixed to Normal Form','h1':'Normal Form','link':'/normal-form'},
    'f4':{'q1':'Divide Fraction by Whole Number','h1':'Fraction Division','link':'/divide-with-whole'},
    'f5':{'q1':'Add or Subtract Two Fractions','h1':'Fraction Operation','link':'/unlike-add'}}
    return render_template('easy_qts_choice.html' , topic=full,unit='UNIT: Fractions')


@app.route('/algebra-intermediate')
def algebra_intermediate():
    full={'f1':{'q1':'Addition of Algebraic Expressions','h1':'Horizontal Addition','link':'/algebra-add'},
    'f2':{'q1':'Subtraction of Algebraic Expressions','h1':'Vertical Subtraction','link':'/vertical_sub'}}
    return render_template('easy_qts_choice.html' , topic=full,unit='UNIT: Algebra')


@app.route('/fraction-easy')
def fraction_easy():
    full={'f1':{'q1':'Convert to Simplest Form','h1':'Simplest Form','link':'/simplest-form'},
    'f2':{'q1':'Find Quotient and Remainder','h1':'Fraction Division','link':'/division'},
    'f3':{'q1':'Add / Subtract like Fraction','h1':'Fraction Operation','link':'/add-fractions'},
    'f4':{'q1':'Multiply Fraction by Whole Number','h1':'Fraction Multiplication','link':'/multiply-with-whole'}}
    return render_template('easy_qts_choice.html' , topic=full,unit='UNIT: Fractions')


@app.route('/algebra-easy')
def algebra_easy():
    full={'f1':{'q1':'Find Coefficient of Terms','h1':'Find Coefficient','link':'/coefficient'},
    'f2':{'q1':'Find value of Variable','h1':'Find value','link':'/value-of-expression'},
    'f3':{'q1':'Classify into Monomial, Bionomial, Trinomial ','h1':'Classification','link':'/monomial'},
    'f4':{'q1':'Identify Like or Unlike','h1':'Identification','link':'/like-unlike'}}
    return render_template('easy_qts_choice.html' , topic=full , unit='UNIT: Algebra')


@app.route('/logout')
def logout():
    session.pop('userid',None)
    return redirect(url_for('index'))


app.secret_key = 'super secret key'
app.run(debug=True)