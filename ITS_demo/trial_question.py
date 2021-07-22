from flask import Flask, render_template, request, flash, redirect, url_for, session
#from flask.ext.session imDortAnacsida
from fractions import Fraction
import random
import os
import math


app = Flask(__name__)


values = [Fraction('25/8'), Fraction('17/4'), Fraction('38/7'), Fraction('29/3'), Fraction('44/5')]
Image_folder = os.path.join('static', 'images')

app.config['UPLOAD_FOLDER'] = Image_folder
full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'cross.jpg')

qtscnt1=0     #fraction
scorecnt1=0   #fraction
qtscnt2 = 0   #algebra
scorecnt2 = 0 #algebra


@app.route("/")
def index():
    return render_template('index_new.html')


@app.route("/login")
def login():
    return render_template('login_new.html')

@app.route("/signup")
def signup():
    return render_template('signup_new.html')


@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/mixed-fraction1", methods=['POST'])
def q1():
    if request.method == 'POST':
        global qtscnt1,scorecnt1
        num = random.randint(1, 100)
        den = random.randint(1, 25)
        while num < den:
            num = random.randint(1, 100)
        que = 'Express as mixed fraction : ' + str(num) + '/' + str(den) + '.'
        quo = num // den
        rem = num % den
        box_ans = [quo, rem, quo, rem, den]
        answer = {'que':que,'ans':box_ans}
        # answer = {'que': que, 'b0': box_ans[0], 'b1': box_ans[1], 'b2': box_ans[2], 'b3': box_ans[3], 'b4': box_ans[4]}
        hint1 = 'Try dividing numerator by denominator'
        hint2 = 'After dividing N/D, quotient =' + str(quo) + ' remainder = ' + str(rem)
        hint3 = 'Mixed Fraction Answer :' + str(quo) + " (" + str(rem) + "/" + str(den) + ")"
        hints = {'h1': hint1, 'h2': hint2, 'h3': hint3}
        total = qtscnt1 * 25
        scoredict = {'score': scorecnt1, 'total': total, 'totalqts': qtscnt1, 'pct': 0}
        return render_template('short_display.html', answer=answer, hints=hints, scoredict=scoredict)
    else:
        return render_template('login.html')


@app.route("/mixed-fraction")
def question():
    global qtscnt1, scorecnt1
    # print(qtscnt)
    # print(scorecnt)
    num = random.randint(1, 100)
    den = random.randint(1, 25)
    while num < den:
        num = random.randint(1, 100)
    que = 'Express as mixed fraction : ' + str(num) + '/' + str(den) + '.'
    quo = num // den
    rem = num % den
    box_ans = [quo, rem, quo, rem, den]
    answer = {'que':que, 'ans':box_ans}
    labels = ['Quotient', 'Remainder', 'Numerator', 'Whole Number', 'Denominator']
    labels = {'labels': labels}
    answer = {'que': que, 'b0': box_ans[0], 'b1': box_ans[1], 'b2': box_ans[2], 'b3': box_ans[3], 'b4': box_ans[4]}
    hint1 = 'Try dividing numerator by denominator'
    hint2 = 'After dividing N/D, quotient =' + str(quo) + ' remainder = ' + str(rem)
    hint3 = 'Mixed Fraction Answer :' + str(quo) + " (" + str(rem) + "/" + str(den) + ")"
    hints = {'h1': hint1, 'h2': hint2, 'h3': hint3}
    total = qtscnt1 * 25
    try:
        tcp = round((scorecnt1/total)*100, 2)
        print(tcp)
    except:
        tcp = 0
    scoredict = {'score': scorecnt1, 'total': total, 'totalqts': qtscnt1, 'tcp': tcp}
  #  return render_template('short_display.html', answer=answer, hints=hints, scoredict=scoredict, labels = labels)
    return render_template('display copy.html', answer=answer, hints=hints, scoredict=scoredict, labels = labels)

#################################################################
@app.route('/score/<tid>/<counter>/<feedback>', methods=['POST'])
# new variable to be added - choice_id
def score(counter, tid, choice_id):
    if request.method == 'POST':
        print('tid : ',tid)
        if tid == 1:
            global scorecnt1, qtscnt1
            marks = 25-(int(counter)*5)
            scorecnt1 += marks
            qtscnt1 += 1
            # print(scorecnt)
            # print(qtscnt)
            # print(marks)
            if marks == 25:
                comment = "Well Done!!!"
            elif 20 <= marks < 25:
                comment = "You have just about mastered it"
            elif 15 <= marks < 20:
                comment = "Keep working on it you are improving"
            else:
                comment = "That's not half bad"
            show_message1 = 'Your points : '+str(marks)+'/25.'
            flash(show_message1)
            flash(comment)
            if qtscnt1 == 4:
                if choice_id == 2:
                    return redirect(url_for(design))
                elif choice_id == 3:
                    return redirect(url_for(display))
                elif choice_id == 1:
                    return redirect(url_for(easy_des))
                else:
                    return redirect(url_for(easy_design))    
            else:
                
                # return render_template('eas')
                return redirect(url_for('question'))
        else:
            global scorecnt2, qtscnt2
            marks = 25-(int(counter)*5)
            scorecnt2 += marks
            qtscnt2 += 1
            # print(scorecnt)
            # print(qtscnt)
            # print(marks)
            if marks == 25:
                comment = "Well Done!!!"
            elif 20 <= marks < 25:
                comment = "You have just about mastered it"
            elif 15 <= marks < 20:
                comment = "Keep working on it you are improving"
            else:
                comment = "That's not half bad"
           
            show_message1 = 'Your points : '+str(marks)+'/25.'
            flash(show_message1)
            flash(comment)
            return redirect(url_for('horizontal_add'))


###############################################################
@app.route("/compare")
def compare():
    num1=random.randint(1,100)
    den1=random.randint(2,25)
    num2 = random.randint(1, 100)
    den2 = random.randint(2, 25)
    f1= Fraction(num1,den1)
    f2= Fraction(num2,den2)
    print('num1 ',num1)
    print('num2 ',num2)
    print('den1 ',den1)
    print('den2 ',den2)
    print('f1', f1)
    print('f2 ',f2)
    # que={'f1':f1,'f2':f2}
    def LCM(a, b):
        return abs(a * b) // math.gcd(a, b)
    que = "Compare "+str(f1)+" and "+str(f2)+" . "
    lcm=LCM(f1.denominator,f2.denominator)
    print(lcm)
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
    print(que)
    print('lcm ',lcm)
    print(eqfrac1,eqfrac2,fract1,fract2)
    box_ans = [lcm,num1,den1,num2,den2,ans]
    answer = {'que':que,'ans':box_ans,'f1':f1,'f2':f2}
    #answer={'que':que,'lcm':lcm,'num1':num1,'den1':den1,'num2':num2,'den2':den2,'ans':ans , 'f1':f1,'f2':f2}
    print(answer)
    h1="LCM of both denominators if Fraction are unlike."
    h2="EXAMPLE : LCM of 5 and 6 is 30."
    h3="Equivalent Fraction of :",str(f1)," => ",num1,"/",den1," and ",str(f2)," => ",num2,"/",den2
    h4=" 4/5 < 5/6."
    hints={'h1':h1,'h2':h2,'h3':h3,'h4':h4}
    total = qtscnt1 * 25
    try:
        tcp = round((scorecnt1/total)*100, 2)
        print(tcp)
    except:
        tcp = 0
    scoredict = {'score': scorecnt1, 'total': total, 'totalqts': qtscnt1, 'tcp': tcp}
    print(hints)
    print(ans)
    l1 = 'Equivalent fraction of ' + str(answer['f1'])
    l2 = 'Equivalent fraction of ' + str(answer['f2'])
    labels = ['LCM',l1,'',l2,'','Solution']
    labels = {'labels':labels}
    return render_template('fracompare.html', answer=answer, hints=hints, scoredict= scoredict)
    #return render_template('compareFraction.html', answer=answer, hints=hints, scoredict= scoredict, labels=labels)


############################################
@app.route("/algebra-add")
def horizontal_add():
    coeff = random.sample(range(-50,50),6) #6 coefficient
    varx = ['x','x\u00b2','x\u00b3'] #x3
    vary = ['y','y\u00b2','y\u00b3'] #y2
    #svarz = ['z','z2','y3'] #z
    rx = random.choice(varx)
    ry = random.choice(vary)
    #rz = random.choice(varz)
    print(coeff)
    sign = []
    for i in coeff[1:6:2]:
        if i < 0:
            sign.append('')
        else:
            sign.append('+')

    haddque = 'Add horizontally '+str(coeff[0])+rx+sign[0]+str(coeff[1])+ry+','+str(coeff[2])+rx+sign[1]+str(coeff[3])+ry+','+str(coeff[4])+rx+sign[2]+str(coeff[5])+ry
    print(haddque)
    x_like = coeff[0:5:2]
    x_sum = sum(x_like)
    y_like = coeff[1:6:2]
    y_sum = sum(y_like)
    answer = {'que':haddque,'varx':rx,'vary':ry,'coeff':coeff,'x_like':x_like,'y_like':y_like,'x_sum':x_sum,'y_sum':y_sum}
    h1 = 'Rearrange into like terms (coefficients with same variable and power)'
    h2 = 'Add coefficientts of like terms'
    h3 = 'Solution : '+str(x_sum)+rx+'+'+str(y_sum)+ry+'.'
    hints = {'h1':h1,'h2':h2,'h3':h3}    
    global qtscnt2, scorecnt2
    total = qtscnt2 * 25
    try:
        pct = round((scorecnt2/total)*100,2)
    except:
        pct = 0
    scoredict = {'score': scorecnt2, 'total': total, 'totalqts': qtscnt2, 'pct': pct}
    return render_template('algebra_add.html', answer=answer, hints=hints, scoredict=scoredict)


############################################
@app.route('/vertical_sub')
def vertical_sub():
    coeff = random.sample(range(-50, 50), 6)  # 6 coefficient
    varx = ['x', 'x\u00b2', 'x\u00b3']  # x3
    vary = ['y', 'y\u00b2', 'y\u00b3']  # y2
    varz = ['z', 'z\u00b2', 'z\u00b3']  # z
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
    print(haddque)
    x_diff = coeff[0] - coeff[3]
    y_diff = coeff[1] - coeff[4]
    z_diff = coeff[2] - coeff[5]
    answer = {'que': haddque, 'varx': rx, 'vary': ry,'varz':rz,'coeff': coeff,'x_diff': x_diff, 'y_diff': y_diff,'z_diff':z_diff}
    h1 = 'Rearrange into like terms (coefficients with same variable and power)'
    h2 = 'Add coefficientts of like terms'
    h3 = 'Solution : ' + str(x_diff) + rx + '+' + str(y_diff) + ry + ' + ' + str(z_diff) + rz + '.'
    hints={'h1':h1,'h2':h2,'h3':h3}
    # print(x_sum,y_sum,z_sum)
    print(hints)

    global qtscnt2, scorecnt2
    total = qtscnt2 * 25
    try:
        pct = round((scorecnt2 / total) * 100, 2)
    except:
        pct = 0
    scoredict = {'score': scorecnt2, 'total': total, 'totalqts': qtscnt2, 'pct': pct}
    return render_template('vertical_sub.html', answer=answer, hints=hints, scoredict=scoredict)

@app.route('/simplest-form')
def simplest_form():
    num = random.randint(1,50)
    den = random.randint(2,50)
    que = "Find simplest form of fraction "+ str(num)+"/"+ str(den)
    simple = Fraction(num, den)
    answer = {'que': que, 'num_ans': simple.numerator, 'den_ans': simple.denominator}
    print(answer)
    scoredict={}
    hints={}
    return render_template('simplestForm.html',answer=answer,hints=hints,scoredict=scoredict)


#simplest_form()

#mixed to normal form
@app.route('/normal-form')
def mixed_to_normal():
    num = random.randint(1,50)
    den = random.randint(2,50)
    whole = random.randint(2,20)
    que = "Convert "+str(whole)+" "+str(num)+"/"+str(den)+" to normal form and find simplest form"
    num_ans = (den*whole)+num
    frac = Fraction(num_ans,den)
    answer = {'que':que, 'num_ans':frac.numerator, 'den_ans':frac.denominator,'den':den,'num':num_ans}
    print(frac.numerator)
    # print(answer)
    # scoredict = 0
    # hints = {}
    # return render_template('normalForm.html', answer=answer, hints=hints, scoredict=scoredict)
    den_ans=den
    whole_ans=whole
    num1=num
    frac = Fraction(num_ans,den_ans)
    #answer = {'que':que, 'num_ans':num_ans, 'den_ans':den_ans,'whole_ans':whole_ans,'num1':num1}
    print(answer)
    h1 = 'Rearrange into like terms (coefficients with same variable and power)'
    h2 = 'Add coefficientts of like terms'
    h3 = 'Solution : ' + str(num_ans)+ '/' + str(den)
    hints = {'h1': h1, 'h2': h2, 'h3': h3}
    global qtscnt2, scorecnt2
    total = qtscnt2 * 25
    try:
        pct = round((scorecnt2 / total) * 100, 2)
    except:
        pct = 0
    scoredict = {'score': scorecnt2, 'total': total, 'totalqts': qtscnt2, 'pct': pct}
    return render_template('normal-form.html', answer=answer, hints=hints, scoredict=scoredict)
    # return render_template('normalForm.html', answer=answer, hints=hints, scoredict=scoredict)

@app.route('/unlike-add')
def unlike_add():
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


    answer = {'que': que, 'num_ans': ans_frac.numerator, 'den_ans': ans_frac.denominator, 'den': den_ans, 'num': num_ans,'num1':num1,'den1':den1,'num2':num2,'den2':den2,'q':que}
    # global qtscnt2, scorecnt2
    # total = qtscnt2 * 25
    # try:
    #     pct = round((scorecnt2 / total) * 100, 2)
    # except:
    #     pct = 0
    # scoredict = {'score': scorecnt2, 'total': total, 'totalqts': qtscnt2, 'pct': pct}
    print(answer)
    h1 = 'Rearrange into like terms (coefficients with same variable and power)'
    h2 = 'Add coefficientts of like terms'
    h3 = 'Solution : ' + str(num_ans) + '/' + str(den_ans)
    hints = {'h1': h1, 'h2': h2, 'h3': h3}
    global qtscnt2, scorecnt2
    total = qtscnt2 * 25
    try:
        pct = round((scorecnt2 / total) * 100, 2)
    except:
        pct = 0
    scoredict = {'score': scorecnt2, 'total': total, 'totalqts': qtscnt2, 'pct': pct}
    return render_template('unlike-add.html', answer=answer, hints=hints, scoredict=scoredict)


# Algebra Easy
@app.route('/p')
def a_easy():
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
        # answer= c1*var1 + s1 + c2*var2 + s2 + c3*var3
        terms.append(term)      
        answers.append(answer) 
        cnt += 1

    return render_template('algebra_easy.html', easy={'question': q4, 'options': terms, 'answer': answers, 'num': 2})
        
def find_term(v, a):
    return a.index(v)


@app.route('/coefficient')
def coefficient():
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
    return render_template('algebra_easy.html', easy={'question': q1, 'options': terms, 'answer': answers, 'num': 1})


@app.route('/monomial')
def monomial():
    terms2 = ['2y + 14z', '20', 'a\u00b2 + b\u00b2 - 2ab', '8xy']
    q2 = 'Classify into monomials, binomials and trinomials'
    variable = ["x", "y", "z", "xy", "yz", "xz", "xyz"]
    sign = ["+", "-"]
    answers = []
    terms = []
    # x = random.randint(1, 4)
    count = 0
    while count <= 3:
        x = random.randint(1, 3)
        answer = ""
        if x == 1:
            answer = "Monomial"
            term = str(random.randint(1, 25)) + random.choice(variable)
            # print(term)
        elif x == 2:
            answer = "Binomial"
            term = str(random.randint(1, 25)) + random.choice(variable) + random.choice(sign) + str(random.randint(1, 25)) + random.choice(variable)
        elif x == 3:
            answer = "Trinomial"
            term = str(random.randint(1, 25)) + random.choice(variable) + random.choice(sign) + str(
                random.randint(1, 25)) + random.choice(variable) + random.choice(sign) + str(
                random.randint(1, 25)) + random.choice(variable)
        answers.append(answer)
        print(answers)
        terms.append(term)
        count += 1


    return render_template('algebra2.html', easy={'question': q2, 'options': terms, 'answer': answers, 'num': 1})



@app.route("/like-unlike")
def like_unlike():
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
    return render_template('algebra2.html', easy={'question': q3, 'options': terms, 'answer': answers, 'num': 2})

@app.route('/division')
def division():
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
    print(q)
    contexts={'ans_num':ans_num,'ans_den':ans_den,'q':q, 'label1': 'Quotient', 'label2': 'Remainder'}

    return render_template('division.html',contexts=contexts)


@app.route('/add-easy')
def add_easy():
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
    contexts={'ans_num':ans_num,'ans_den':ans_den,'q':q, 'label1': 'Quotient', 'label2' : 'Remainder'}
    return render_template('division.html',contexts=contexts)


@app.route('/whole')
def whole():
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
    # print(q)
    return render_template('division.html',contexts={'ans_num':ans_num,'ans_den':ans_den,'q':q, 'label1': 'Numerator', 'label2': 'Denominator'})


@app.route('/number-line')
def number_line():
    x = random.randint(0, 10)
    que = 'Plot fraction '+ str(x)+'/10 on number line'
    return render_template('number_line.html', nums = {'que': que, 'ans': x})


#########################################
@app.route('/divide-whole')
def divide_whole():
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
    context={'que':que,'numerator':numerator,'hints':hints,'denominator':denominator,'ans_num':ans_num,'ans_den':ans_den,'rec_num':1,'rec_den':div}
    scoredict = {'score': "", 'total': "", 'totalqts': "", 'pct': ""}
    return render_template('divideby_whole.html',answer=context,scoredict=scoredict,hints=hints)

##########################################################
#2
@app.route('/fraction-intermediate')
def fraction_intermediate():
    full={'f1':{'q1':'Expressed as Mixed Fraction','h1':'Mixed Fraction','link':'/mixed-fraction'},
    'f2':{'q1':'Compare Two Fraction','h1':'Compare','link':'/compare'},
    'f3':{'q1':'Convert Mixed to Normal Form','h1':'Normal Form','link':'/normal-form'},
    'f4':{'q1':'Divide Fraction by Whole Number','h1':'Fraction Division','link':'/divide-whole'},
    'f5':{'q1':'Add or Subtract Two Fractions','h1':'Fraction Operation','link':'/unlike-add'}}
    return render_template('easy_qts_choice.html' , topic=full,unit='UNIT: Fractions')
    # return render_template('question_display_design.html')

#######################################################
#4
@app.route('/algebra-intermediate')
def algebra_intermediate():
    # return render_template('algebra_qts_design.html')
    full={'f1':{'q1':'Addition of Algebraic Expressions','h1':'Horizontal Addition','link':'/algebra-add'},
    'f2':{'q1':'Subtraction of Algebraic Expressions','h1':'Vertical Subtraction','link':'/vertical_sub'}}
    return render_template('easy_qts_choice.html' , topic=full,unit='UNIT: Algebra')
    
#########################################################
#1
@app.route('/fraction-easy')
def fraction_easy():
    full={'f1':{'q1':'Convert to Simmplest Form','h1':'Simplest Form','link':'/simplest-form'},
    'f2':{'q1':'Find Quotient and Remainder','h1':'Fraction Division','link':'/division'},
    'f3':{'q1':'Add / Subtract like Fraction','h1':'Fraction Operation','link':'/add-easy'},
    'f4':{'q1':'Multiply Fraction by Whole Number','h1':'Fraction Multiplication','link':'/whole'}}
    return render_template('easy_qts_choice.html' , topic=full,unit='UNIT: Fractions')


#########################################################
#3
@app.route('/algebra-easy')
def algebra_easy():
    
    full={'f1':{'q1':'Find Coefficient of Terms','h1':'Find Coefficient','link':'/coefficient'},
    'f2':{'q1':'Find value of Variable','h1':'Find value','link':'/p'},
    'f3':{'q1':'Classify into Monomial, Bionomial, Trinomial ','h1':'Classification','link':'/monomial'},
    'f4':{'q1':'Identify Like or Unlike','h1':'Identification','link':'/like-unlike'}}
    return render_template('easy_qts_choice.html' , topic=full , unit='UNIT: Algebra')


app.secret_key = 'super secret key'
app.run(debug=True)